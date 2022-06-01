from Projekat.DatabaseCRUD.CRUDAbstract import CRUD
from mysql.connector import connect, Error


class CrudPotrosnjaBrojila(CRUD):

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def read(self, *args):
        _id = args[0]
        _mesec = args[1]
        try:
            with connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
            ) as connecting:
                query = ""
                with connecting.cursor(prepared=True) as cursor:
                    #TO DO
                    pass
        except Error as e:
            print(e)

    def insert(self, *args):
        _id = args[0]
        _mesec = args[1]
        _potrosnja = args[2]
        try:
            with connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
            ) as connecting:
                query = ""
                with connecting.cursor(prepared=True) as cursor:
                    #TO DO
                    pass
        except Error as e:
            print(e)

    def delete(self, *args):
        pass

    def update(self, *args):
        pass