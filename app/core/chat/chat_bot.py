import logging
import socket
import threading
import time
from typing import Optional

class ChatBot:
    def __init__(self, set_latest_votes, get_latest_votes):
        self._server = "irc.chat.twitch.tv"
        self._port = 6667
        self._nickname = "TwitchGo_bot"
        self._token = "oauth:nnz481ral6ao5zt5bqhes4mw01womg"  # Note: Store tokens securely!
        self._channel = "#knr_bionik_tv"
        self._set_votes = set_latest_votes
        self._get_latest_votes = get_latest_votes

        self._sock: Optional[socket.socket] = None
        self._stop_event = threading.Event()
        self._reconnect_delay = 5  # Initial wait time before retrying connection (seconds)
        self._max_reconnect_delay = 300  # Maximum wait time before retrying connection (seconds)

        self._lock = threading.Lock()
        self._connect()

    def _connect(self):
        """Initialize connection to Twitch IRC server."""
        with self._lock:
            if self._sock:
                self._sock.close()
            self._sock = socket.socket()
            try:
                logging.info(f"Connecting to {self._server}:{self._port}")
                self._sock.connect((self._server, self._port))
                self._sock.send(f"PASS {self._token}\n".encode('utf-8'))
                self._sock.send(f"NICK {self._nickname}\n".encode('utf-8'))
                self._sock.send(f"JOIN {self._channel}\n".encode('utf-8'))
                logging.info("Connection established.")
                self._reconnect_delay = 5  # Reset delay after successful connection
            except Exception as e:
                logging.error(f"Error during connection: {e}")
                self._schedule_reconnect()

    def _schedule_reconnect(self):
        """Schedule reconnection to the server."""
        if self._stop_event.is_set():
            return
        logging.info(f"Retrying connection in {self._reconnect_delay} seconds.")
        threading.Thread(target=self._reconnect, daemon=True).start()

    def _reconnect(self):
        """Attempt to reconnect to the IRC server."""
        while not self._stop_event.is_set():
            try:
                time.sleep(self._reconnect_delay)
                self._connect()
                if self._sock:
                    break  # Successful connection
            except Exception as e:
                logging.error(f"Error during reconnection: {e}")
            self._reconnect_delay = min(self._reconnect_delay * 2, self._max_reconnect_delay)  # Exponential Backoff

    def _listen(self):
        """Infinite loop listening for messages from the IRC server."""
        while not self._stop_event.is_set():
            try:
                resp = self._sock.recv(2048).decode('utf-8')
                if not resp:
                    logging.warning("Empty reception. Disconnected.")
                    self._schedule_reconnect()
                    break

                for line in resp.strip().split('\r\n'):
                    self._handle_message(line)
            except socket.error as e:
                logging.error(f"Socket error: {e}")
                self._schedule_reconnect()
                break
            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                self._schedule_reconnect()
                break

    def _handle_message(self, message: str):
        """Process a single message from the IRC server."""
        if message.startswith("PING"):
            self._sock.send("PONG\n".encode('utf-8'))
            logging.debug("Sent PONG in response to PING.")
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

        logging.info(f"[MESSAGE] {username}: {msg_content}")

        if len(message_list) > 1 and message_list[0].startswith('!'):
            command = message_list[0]
            argument = message_list[1]

            if command == "!vote":
                self.vote(username, argument)

    def run(self):
        """Start the listening thread."""
        threading.Thread(target=self._listen, daemon=True).start()

    def stop(self):
        """Stop the bot."""
        self._stop_event.set()
        with self._lock:
            if self._sock:
                self._sock.close()

    def vote(self, username: str, vote_argument: str):
        """Handle the voting command."""
        if self.can_vote(username):
            votes = self._get_latest_votes()
            if vote_argument in votes:
                votes[vote_argument].add_vote(username)
                logging.info(f"{username} votes for {vote_argument}")
            else:
                logging.warning(f"{username} tried to vote for a non-existing bonus: {vote_argument}")

    def can_vote(self, username: str) -> bool:
        """Check if a user can vote."""
        votes = self._get_latest_votes()
        for option in votes.values():
            if username in option.get_votes():
                return False
        return True
