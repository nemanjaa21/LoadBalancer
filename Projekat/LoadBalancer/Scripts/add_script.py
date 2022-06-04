from Projekat.DatabaseCRUD.databaseCRUD import DatabaseCRUD


class Add_script:

    def manual_adding(self, msg):
        _db = DatabaseCRUD()

        _tokens = msg.split(':')
        _id = _tokens[1]

        _ret = _db.get_brojilo(_id)
        if not _ret:
            print("[MAIN THREAD] Brojilo sa id='{id}' ne postoji!".format(id=_id))
        else:
            _mesec = _tokens[2]
            _ret = _db.get_potrosnja_brojila(_id, _mesec)

            if not _ret:
                _potrosnja = _tokens[3]
                _ret = _db.insert(_id, _mesec, _potrosnja)
                print("[MAIN THREAD] {ret}!".format(ret=_ret))
            else:
                print("[MAIN THREAD] Merenje brojila id:mesec='{id}:{mesec}' vec postoji!".format(id=_id, mesec=_mesec))

    def automatic_adding(self, msg, buffer):
        buffer.append(msg)
