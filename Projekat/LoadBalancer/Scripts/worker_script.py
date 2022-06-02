from Projekat.Worker.worker import Worker
import threading


class Worker_script:

    def new_worker(self, conn, number_of_workers, workers):
        number_of_workers = number_of_workers + 1
        _worker = Worker(f'WORKER_{number_of_workers - 1}')
        t = threading.Thread(target=_worker.start_worker, name=f'WORKER_{number_of_workers - 1}')
        print(f'[NEW WORKER] client created new worker!')
        t.start()

        workers.append(_worker)
        _result = f"WORKER_{number_of_workers - 1} uspesno dodat!"
        conn.send(_result.encode('utf-8'))
        return number_of_workers

    def terminate_worker(self, name, workers, number_of_workers):
        if name != "WORKER_0":
            for _worker in workers:
                if _worker.name == name:
                    _worker.queue_put("!TERM")
                    workers.remove(_worker)
                    print("[{name}] Terminated".format(name=_worker.name))
                    number_of_workers = number_of_workers - 1
        return number_of_workers