import re
import socket
import sys
import os


class Twitch:

    def __init__(self, user, key):
        self.user = user
        self.oauth = key
        self.connection_to_twitch = None

    def __enter__(self):
        self._open_connection_to_twitch()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection_to_twitch.close()

    def _open_connection_to_twitch(self):
        print("Connecting to twitch.tv")
        self.connection_to_twitch = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection_to_twitch.settimeout(0.6)
        connect_host = "irc.twitch.tv"
        connect_port = 6667
        try:
            self.connection_to_twitch.connect((connect_host, connect_port))
        except Exception as e:
            print(f"Failed to connect to twitch: {e}")
            sys.exit(1)

    def _send_user_details(self):
        print("Sending our details to twitch...")
        self.connection_to_twitch.send('USER %s\r\n' % self.user)
        self.connection_to_twitch.send('PASS %s\r\n' % self.oauth)
        self.connection_to_twitch.send('NICK %s\r\n' % self.user)

    def twitch_connect(self):
        print("Connected to twitch")
        self._open_connection_to_twitch()
        self._send_user_details()

        if not Twitch.twitch_login_status(self.connection_to_twitch.recv(1024)):
            print("... and they didn't accept our details")
            sys.exit(1)

        print("... they accepted our details!")
        print("Connected to twitch.tv!")

        self.connection_to_twitch.send('JOIN #%s\r\n' % self.user)
        self.connection_to_twitch.recv(1024)

    @staticmethod
    def twitch_login_status(data):
        if re.match(r'^:(testserver\.local|tmi\.twitch\.tv) NOTICE \* :Login unsuccessful\r\n$', data):
            return False
        return True

    @staticmethod
    def check_has_message(data):
        return re.match(r'^:[a-zA-Z0-9_]+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+(\.tmi\.twitch\.tv|\.testserver\.local) PRIVMSG #[a-zA-Z0-9_]+ :.+$', data)

    @staticmethod
    def parse_message(data):
        return {
            'channel': re.findall(r'^:.+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+.+ PRIVMSG (.*?) :', data)[0],
            'username': re.findall(r'^:([a-zA-Z0-9_]+)\!', data)[0],
            'message': re.findall(r'PRIVMSG #[a-zA-Z0-9_]+ :(.+)', data)[0].decode('utf8')
        }

    def twitch_receive_messages(self, amount=1024):
        data = None
        try:
            data = self.connection_to_twitch.recv(amount)
        except Exception as e:
            print(f"Unable to receive data: {e}")
            return False

        if not data:
            print("Lost connection to Twitch, attempting to reconnect...")
            self.twitch_connect()
            return None

        # self.ping(data)

        if Twitch.check_has_message(data):
            return [Twitch.parse_message(line) for line in filter(None, data.split(os.linesep))]
