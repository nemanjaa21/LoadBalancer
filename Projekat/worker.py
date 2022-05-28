import threading
from queue import Queue
from databaseCRUD import *


class Worker:

    def __init__(self):
        self.q = Queue()
        self.is_free = True

    def start_worker(self):
        #TO DO

    def queue_put(self, q):
        self.q.put(q)

    def check(self):
        return self.is_free

    def do_work(self, item):
        #TO DO
