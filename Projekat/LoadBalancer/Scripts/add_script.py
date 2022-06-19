from Projekat.DatabaseCRUD.databaseCRUD import DatabaseCRUD


class Add_script:

    @staticmethod
    def manual_adding(msg, db='RES_PROJEKAT'):
        _db = DatabaseCRUD('127.0.0.1', 'admin', 'admin', db)

        _tokens = msg.split(':')
        _id = _tokens[1]

        _ret = _db.get_brojilo(_id)
        if not _ret:
            print("[MAIN THREAD] Brojilo sa id='{id}' ne postoji!".format(id=_id))
            return -1
        else:
            _mesec = _tokens[2]
            _ret = _db.get_potrosnja_brojila(_id, _mesec)

            if not _ret:
                _potrosnja = _tokens[3]
                _ret = _db.insert(_id, _mesec, _potrosnja)
                if _ret == 1:
                    _ret = f"Successfully inserted '{_id} {_mesec} {_potrosnja}'"
                print("[MAIN THREAD] {ret}!".format(ret=_ret))
                return 0
            else:
                print("[MAIN THREAD] Merenje brojila id:mesec='{id}:{mesec}' vec postoji!".format(id=_id, mesec=_mesec))
                return -2

    @staticmethod
    def automatic_adding(msg, buffer):
        buffer.append(msg)
        return len(buffer)
