from Projekat.DatabaseCRUD.databaseCRUD import DatabaseCRUD as db


class Add_script:

    def manual_adding(self, msg):
        ret = db.get_brojilo(msg[7:])
        for r in ret:
            print(r)

    def automatic_adding(self, msg, buffer):
        # TO DO
        pass
