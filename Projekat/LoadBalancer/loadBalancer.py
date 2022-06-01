import socket
import threading

from Scripts.worker_script import Worker_script
from Scripts.add_script import Add_script

from Projekat.Worker.worker import Worker


class LoadBalancer:

    def __init__(self):
        self.port = 8000
        self.server = socket.gethostbyname(socket.gethostname())
        self.address = (self.server, self.port)
        self.format = 'utf-8'

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(self.address)

        self.workers = []
        self.number_of_workers = 1
        self.buffer = list()

        self.worker_script = Worker_script()
        self.add_script = Add_script()

    def handle(self, conn, addr):
        #TO DO
        pass

    def start(self):
        self.server.listen()
        print(f'[LISTENING] server listening at {self.address}...')
        _worker = Worker("WORKER_0")
        _t = threading.Thread(target=_worker.start_worker, name=f'WORKER_0')
        _t.start()
        self.workers.append(_worker)
        while True:
            _conn, _addr = self.server.accept()
            _thread = threading.Thread(target=self.handle, args=(_conn, _addr))
            _thread.start()

    def buffer_check(self):
        #TO DO
        pass


def main():
    _server = LoadBalancer()
    _server.start()


if __name__ == '__main__':
    main()
