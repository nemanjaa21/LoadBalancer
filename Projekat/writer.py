import socket


class Writer:

    def __init__(self):
        self.port = 8000
        self.server = socket.gethostbyname(socket.gethostname())
        self.address = (self.server, self.port)
        self.format = 'utf-8'

        self.writer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.writer.connect(self.address)
        self.connected = True

    def send_message(self, message):
        self.writer.send(message.encode(self.format))

    def writer_UI(self):
        #TO DO

def main():
    writer = Writer()
    writer.writer_UI()


if __name__ == "__main__":
    main()
