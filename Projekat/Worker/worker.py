import threading
from queue import Queue
from Projekat.DatabaseCRUD.databaseCRUD import DatabaseCRUD


class Worker:

    def __init__(self, name):
        self.q = Queue()
        self.is_free = True
        self.name = name
        self.db = DatabaseCRUD()

    def start_worker(self):
        #TO DO
        pass

    def queue_put(self, q):
        self.q.put(q)

    def check(self):
        return self.is_free

    def do_work(self, item):
        #TO DO
        pass
