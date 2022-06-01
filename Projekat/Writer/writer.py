import socket
from ClientUI import ClientUI


class Client:

    def __init__(self):
        self.port = 8000
        self.server = socket.gethostbyname(socket.gethostname())
        self.address = (self.server, self.port)
        self.format = 'utf-8'

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.address)
        self.connected = True
        self.menu = ClientUI()

    def send_message(self, message):
        self.client.send(message.encode(self.format))

    def client_UI(self):
        #TO DO
        pass


def main():
    client = Client()
    client.client_UI()


if __name__ == "__main__":
    main()
