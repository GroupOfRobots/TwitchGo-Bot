import socket
import threading


class ChatBot:
    def __init__(self, set_latest_votes):
        self._sock = socket.socket()
        self._server = "irc.chat.twitch.tv"
        self._port = 6667
        self._nickname = "nienawidzekomarow"
        self._token = "oauth:nnz481ral6ao5zt5bqhes4mw01womg"
        self._channel = "#knr_bionik_tv"
        self._user_votes = [[], []]
        self._set_votes = set_latest_votes

        self.connect()

    def connect(self):
        self._sock.connect((self._server, self._port))

        self._sock.send(f"PASS {self._token}\n".encode('utf-8'))
        self._sock.send(f"NICK {self._nickname}\n".encode('utf-8'))
        self._sock.send(f"JOIN {self._channel}\n".encode('utf-8'))

    def response(self):
        resp = self._sock.recv(2048).decode('utf-8')

        if resp == "":
            self.run()

        if resp.split(self._channel)[0].split('!')[0].split()[0] == "PING":
            self.run()

        username = resp.split(self._channel)[0].split('!')[0][1:].strip()
        message = resp.split(self._channel)[-1][2:].strip()

        command, argument = message.split()[:2]

        if command == "!vote":
            self.vote(username, int(argument))

        self.run()

    def run(self):
        resp = threading.Thread(target=self.response, daemon=True)
        resp.start()

    def vote(self, username, team_number_str):
        try:
            team_number = int(team_number_str)
        except ValueError:
            return
        if 0 < team_number < 3:
            self.save_vote(username, team_number)

    def save_vote(self, username, team_number):
        if username not in self._user_votes[0] and \
                username not in self._user_votes[1]:
            self._user_votes[team_number-1].append(username)

        votes = {len(self._user_votes[0]): len(self._user_votes[1])}

        self._set_votes(votes)
