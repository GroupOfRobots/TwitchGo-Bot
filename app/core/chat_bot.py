import socket
import threading
import logging


class ChatBot:
    def __init__(self, set_latest_votes, get_latest_votes):
        self._sock = socket.socket()
        self._server = "irc.chat.twitch.tv"
        self._port = 6667
        self._nickname = "TwitchGo_bot"
        self._token = "oauth:nnz481ral6ao5zt5bqhes4mw01womg"
        self._channel = "#knr_bionik_tv"
        self._set_votes = set_latest_votes
        self._get_latest_votes = get_latest_votes

        self.connect()

    def connect(self):
        self._sock.connect((self._server, self._port))

        self._sock.send(f"PASS {self._token}\n".encode('utf-8'))
        self._sock.send(f"NICK {self._nickname}\n".encode('utf-8'))
        self._sock.send(f"JOIN {self._channel}\n".encode('utf-8'))

    def response(self):
        try:
            resp = self._sock.recv(2048).decode('utf-8')
        except ConnectionResetError:
            self.connect()
            resp = self._sock.recv(2048).decode('utf-8')

        if resp == "":
            self.run()

        if resp.split(self._channel)[0].split('!')[0].split()[0] == "PING":
            self.run()

        username = resp.split(self._channel)[0].split('!')[0][1:].strip()
        message = resp.split(self._channel)[-1][2:].strip()

        print(f"{username}: {message}")
        logging.info(f"[MESSAGE] {username}: {message}")
        message_list = message.split()

        if len(message_list) > 1 and message_list[0][0] == '!':
            command = message_list[0]
            argument = message_list[1]

            if command == "!vote":
                self.vote(username, argument)

        self.run()

    def run(self):
        resp = threading.Thread(target=self.response, daemon=True)
        resp.start()

    def vote(self, username, vote_argument):
        if self.can_vote(username):
            if vote_argument in self._get_latest_votes().keys():
                self._get_latest_votes()[vote_argument].add_vote(username)

    def can_vote(self, username):
        for option in self._get_latest_votes().keys():
            if username in self._get_latest_votes()[option].get_votes:
                return False
        return True
