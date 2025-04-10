# tests/test_chat_bot.py

import unittest
from unittest.mock import patch, MagicMock
from app.core.chat.chat_bot import ChatBot


class TestChatBot(unittest.TestCase):
    @patch('socket.socket')
    def test_chat_bot_initialization(self, mock_socket):
        set_latest_votes = MagicMock()
        get_latest_votes = MagicMock()
        chat_bot = ChatBot(set_latest_votes, get_latest_votes)

        # Sprawdzenie, czy socket został utworzony i połączony
        mock_socket.assert_called_once()
        chat_bot._sock.connect.assert_called_with(("irc.chat.twitch.tv", 6667))
        chat_bot._sock.send.assert_any_call(b"PASS oauth:nnz481ral6ao5zt5bqhes4mw01womg\n")
        chat_bot._sock.send.assert_any_call(b"NICK TwitchGo_bot\n")
        chat_bot._sock.send.assert_any_call(b"JOIN #knr_bionik_tv\n")

    @patch('socket.socket')
    def test_handle_message_ping(self, mock_socket):
        set_latest_votes = MagicMock()
        get_latest_votes = MagicMock()
        chat_bot = ChatBot(set_latest_votes, get_latest_votes)

        # Mockowanie metody _handle_message
        with patch.object(chat_bot, '_handle_message', wraps=chat_bot._handle_message) as mock_handle:
            # Symulacja odebrania wiadomości PING
            chat_bot._sock.recv.return_value = b"PING :tmi.twitch.tv\r\n"
            with patch('builtins.print') as mock_print:
                chat_bot._listen()

                # Sprawdzenie, czy PONG został wysłany
                chat_bot._sock.send.assert_called_with(b"PONG\n")

    @patch('socket.socket')
    def test_handle_message_vote_command(self, mock_socket):
        set_latest_votes = MagicMock()
        get_latest_votes = MagicMock()

        # Mockowanie zwracania głosów
        mock_vote_option = MagicMock()
        get_latest_votes.return_value = {"Bonus1": mock_vote_option}

        chat_bot = ChatBot(set_latest_votes, get_latest_votes)

        # Symulacja odebrania wiadomości z komendą !vote
        vote_message = ":user1!user1@user1.tmi.twitch.tv PRIVMSG #knr_bionik_tv :!vote Bonus1\r\n"
        chat_bot._sock.recv.return_value = vote_message.encode('utf-8')

        with patch.object(chat_bot, 'vote') as mock_vote:
            with patch('builtins.print') as mock_print:
                chat_bot._listen()
                mock_vote.assert_called_with("user1", "Bonus1")

    @patch('socket.socket')
    def test_stop_chat_bot(self, mock_socket):
        set_latest_votes = MagicMock()
        get_latest_votes = MagicMock()
        chat_bot = ChatBot(set_latest_votes, get_latest_votes)

        with patch.object(chat_bot, '_stop_event', autospec=True) as mock_stop_event:
            chat_bot.stop()
            mock_stop_event.set.assert_called_once()
            chat_bot._sock.close.assert_called_once()


if __name__ == '__main__':
    unittest.main()
