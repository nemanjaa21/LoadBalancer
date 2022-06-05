import socket
import threading
import time

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
        print(f'[NEW CONNECTION] {addr} connected.')

        is_connected = True

        while is_connected:
            _msg = conn.recv(1024).decode(self.format)
            if _msg:
                if _msg == '!DISC':
                    is_connected = False
                elif 'Manual' in _msg:
                    self.add_script.manual_adding(_msg)
                elif 'Name ' in _msg:
                    self.number_of_workers = self.worker_script.terminate_worker(_msg.split()[1], self.workers,
                                                                                 self.number_of_workers)
                elif _msg == 'add':
                    self.number_of_workers = self.worker_script.new_worker(conn, self.number_of_workers, self.workers)
                    self.buffer_check()
                else:
                    self.add_script.automatic_adding(_msg, self.buffer)
                    self.buffer_check()

        print(f'[THREAD {threading.current_thread().ident}] Terminated')
        conn.close()

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

        if len(self.buffer) >= 10:
            _in = list()
            for _item in self.buffer:
                _in.append(_item)
                if len(_in) == 10:
                    break
            _done = False

            while not _done:
                for _worker in self.workers:
                    if _worker.check():
                        _worker.queue_put(_in)
                        _done = True
                        break
                if not _done:
                    time.sleep(2)
            for _item in _in:
                self.buffer.remove(_item)


def main():
    _server = LoadBalancer()
    _server.start()


if __name__ == '__main__':
    main()
