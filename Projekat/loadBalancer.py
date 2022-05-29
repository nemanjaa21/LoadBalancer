import socket
import threading

from databaseCRUD import *

from worker import Worker

PORT = 8000
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDRESS)

workers = []
number_of_workers = 1
buffer = list()


def terminate_worker(name):
    #TO DO


def new_worker(conn):
    #TO DO


def automatic_adding(msg):
    #TO DO


def manual_adding(msg):
    #TO DO


def buffer_check():
    #TO DO


def handle(conn, addr):
    #TO DO


def start():
    server.listen()
    print(f'[LISTENING] server listening at {ADDRESS}...')
    _worker = Worker()
    t = threading.Thread(target=_worker.start_worker, name=f'WORKER_0')
    t.start()
    workers.append(_worker)

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle, args=(conn, addr))
        thread.start()


def main():
    start()


if __name__ == '__main__':
    main()
