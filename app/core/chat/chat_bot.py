# app/core/chat/chat_bot.py

import logging
import socket
import threading
import time

class ChatBot:
    def __init__(self, set_latest_votes, get_latest_votes):
        self._server = "irc.chat.twitch.tv"
        self._port = 6667
        self._nickname = "TwitchGo_bot"
        self._token = "oauth:nnz481ral6ao5zt5bqhes4mw01womg"
        self._channel = "#knr_bionik_tv"
        self._set_votes = set_latest_votes
        self._get_latest_votes = get_latest_votes

        self._sock = None
        self._stop_event = threading.Event()
        self._reconnect_delay = 5
        self._max_reconnect_delay = 300

        self._lock = threading.Lock()
        self._listen_thread = None
        self._connect()

    def _connect(self):
        """Initialize the connection to the IRC server."""
        with self._lock:
            if self._sock:
                try:
                    self._sock.close()
                except Exception as e:
                    logging.error(f"Error closing socket: {e}")
            self._sock = socket.socket()
            try:
                logging.info(f"Łączenie z {self._server}:{self._port}")
                self._sock.connect((self._server, self._port))
                self._sock.send(f"PASS {self._token}\n".encode('utf-8'))
                self._sock.send(f"NICK {self._nickname}\n".encode('utf-8'))
                self._sock.send(f"JOIN {self._channel}\n".encode('utf-8'))
                logging.info("Połączenie nawiązane.")
                self._reconnect_delay = 5  # Reset after successful connection
                # Begin listening for messages
                if not self._listen_thread or not self._listen_thread.is_alive():
                    self._listen_thread = threading.Thread(target=self._listen, daemon=True)
                    self._listen_thread.start()
            except Exception as e:
                logging.error(f"Błąd podczas łączenia: {e}")
                self._schedule_reconnect()

    def _schedule_reconnect(self):
        """Plan the reconnection to the IRC server."""
        if self._stop_event.is_set():
            return
        logging.info(f"Ponawianie połączenia za {self._reconnect_delay} sekund.")
        threading.Thread(target=self._reconnect, daemon=True).start()

    def _reconnect(self):
        """Trying to reconnect to the IRC server."""
        while not self._stop_event.is_set():
            try:
                time.sleep(self._reconnect_delay)
                self._connect()
                if self._sock:
                    break  # Udane połączenie
            except Exception as e:
                logging.error(f"Błąd podczas ponownego łączenia: {e}")
            self._reconnect_delay = min(self._reconnect_delay * 2, self._max_reconnect_delay)

    def _listen(self):
        """Infinitive loop listening for messages from the IRC server."""
        while not self._stop_event.is_set():
            try:
                resp = self._sock.recv(2048).decode('utf-8')
                if not resp:
                    logging.warning("Odebrano pustą wiadomość. Rozłączono.")
                    self._schedule_reconnect()
                    break

                for line in resp.strip().split('\r\n'):
                    self._handle_message(line)
            except socket.error as e:
                logging.error(f"Błąd socketu: {e}")
                self._schedule_reconnect()
                break
            except Exception as e:
                logging.error(f"Niespodziewany błąd: {e}")
                self._schedule_reconnect()
                break

    def _handle_message(self, message: str):
        """Handle the incoming message from the IRC server."""
        if message.startswith("PING"):
            self._sock.send("PONG\n".encode('utf-8'))
            logging.debug("Wysłano PONG w odpowiedzi na PING.")
            return

        parts = message.split(' PRIVMSG ')
        if len(parts) < 2:
            return

        prefix = parts[0]
        msg_content = parts[1].strip()
        if not prefix.startswith(':'):
            return

        username = prefix.split('!')[0][1:]
        message_list = msg_content.split()

        logging.info(f"[WIADOMOŚĆ] {username}: {msg_content}")

        if len(message_list) > 1 and message_list[0].startswith('!'):
            command = message_list[0]
            argument = message_list[1]

            if command.lower() == "!vote":
                self.vote(username, argument)

    def run(self):
        logging.info("ChatBot działa.")

    def stop(self):
        logging.info("Zatrzymywanie ChatBot...")
        self._stop_event.set()
        with self._lock:
            if self._sock:
                try:
                    self._sock.close()
                except Exception as e:
                    logging.error(f"Błąd podczas zamykania socketu: {e}")
        if self._listen_thread:
            self._listen_thread.join()
        logging.info("ChatBot zatrzymany.")

    def vote(self, username: str, vote_argument: str):
        """Support for voting."""
        if self.can_vote(username):
            votes = self._get_latest_votes()
            if vote_argument in votes:
                votes[vote_argument].add_vote(username)
                logging.info(f"{username} głosuje na {vote_argument}")
            else:
                logging.warning(f"{username} próbował głosować na nieistniejący bonus: {vote_argument}")

    def can_vote(self, username: str) -> bool:
        """Check if the user can vote."""
        votes = self._get_latest_votes()
        for option in votes.values():
            if username in option.get_votes():
                return False
        return True
