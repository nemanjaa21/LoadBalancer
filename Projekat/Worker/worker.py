import threading
import time
from queue import Queue
from Projekat.DatabaseCRUD.databaseCRUD import DatabaseCRUD


class Worker:

    def __init__(self, name):
        self.q = Queue()
        self.is_free = True
        self.name = name
        self.db = DatabaseCRUD()

    def start_worker(self):
        while True:
            self.is_free = True
            print("[{name}] is free".format(name=threading.current_thread().name))
            item = self.q.get()
            self.is_free = False
            if item == "!TERM":
                break
            print("[{name}] is busy".format(name=threading.current_thread().name))
            print("[{name}] Message received: {msg}".format(name=threading.current_thread().name, msg=item))
            for i in item:
                self.do_work(i)
                time.sleep(5)
            if item is None:
                self.q.task_done()
                break

    def queue_put(self, q):
        self.q.put(q)

    def check(self):
        return self.is_free

    def do_work(self, item):
        print("[{name}] Processing message '{msg}'".format(name=threading.current_thread().name, msg=item))
        tokens = item.split()
        id_brojila = tokens[0]

        res = self.db.get_brojilo(id_brojila)
        if res:
            mesec = tokens[1]
            res = self.db.get_potrosnja_brojila(id_brojila, mesec)
            if res:
                print("[{name}] '{item}' already exists".format(name=threading.current_thread().name, item=item))
            else:
                potrosnja = tokens[2]
                _msg = self.db.insert(id_brojila, mesec, potrosnja)
                if _msg == 1:
                    _msg = f"Successfully inserted '{id_brojila} {mesec} {potrosnja}'"
                print("[{name}] {msg}".format(name=threading.current_thread().name, msg=_msg))
        else:
            print("[{name}] unknown id = '{id}'".format(name=threading.current_thread().name, id=id_brojila))
        print("[{name}] Message processed '{msg}'\n".format(name=threading.current_thread().name, msg=item))
       
