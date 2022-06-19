from Projekat.Worker.worker import Worker
import threading


class Worker_script:

    @staticmethod
    def new_worker(number_of_workers, workers):
        number_of_workers = number_of_workers + 1
        _worker = Worker(f'WORKER_{number_of_workers - 1}')

        t = threading.Thread(target=_worker.start_worker, name=f'WORKER_{number_of_workers - 1}', daemon=True)
        print(f'[NEW WORKER] client created new worker!')
        t.start()

        workers.append(_worker)
        return number_of_workers

    @staticmethod
    def terminate_worker(name, workers, number_of_workers):
        _flag = 0
        if name != "WORKER_0":
            _flag = 2
            for _worker in workers:
                if _worker.name == name:
                    if not _worker.check():
                        print("[THREAD {id}] {worker} cannot be deleted. Reason: Busy.".format(
                            id=threading.current_thread().ident, worker=name))
                        _flag = - 10
                        break
                    _worker.queue_put("!TERM")
                    workers.remove(_worker)

                    print("[{name})] Terminated".format(name=_worker.name))
                    number_of_workers = number_of_workers - 1
                    Worker_script.reorder_workers(workers, number_of_workers)

                    _flag = 1
                    Worker_script.print_workers(workers)
                    break
        else:
            print("[THREAD {id}] {worker} cannot be deleted. Reason: System worker.".format(
                id=threading.current_thread().ident, worker=name))
        if _flag == 2:
            print("[THREAD {id}] {worker} cannot be deleted. Reason: Doesn't exists.".format(
                id=threading.current_thread().ident, worker=name))
        return number_of_workers

    @staticmethod
    def change_name(workers, number_of_workers, i):
        for j in range(i + 1, number_of_workers):
            _id = int(workers[j].name.split('_')[1])
            workers[j].name = "WORKER_{id}".format(id=_id - 1)

    @staticmethod
    def print_workers(workers):
        print("[LIST OF WORKERS]")
        for _w in workers:
            print("{name}".format(name=_w.name))

    @staticmethod
    def reorder_workers(workers, number_of_workers):
        for i in range(0, number_of_workers - 1):
            _id1 = int(workers[i].name.split('_')[1])
            _id2 = int(workers[i + 1].name.split('_')[1])

            if _id2 - _id1 != 1:
                Worker_script.change_name(workers, number_of_workers, i)
                break
