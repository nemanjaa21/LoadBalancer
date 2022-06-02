from Projekat.DatabaseCRUD.CRUDAbstract import CRUD
from mysql.connector import connect, Error


class CRUDBrojila(CRUD):

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def insert(self, *args):
        #TO DO
        pass

    def delete(self, *args):
        #TO DO
        pass

    def update(self, *args):
        #TO DO
        pass

    def read(self, *args):
        _id = args[0]
        try:
            with connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
            ) as connecting:
                query = f"SELECT * FROM brojilo p where p.IdBrojila = %s;"
                with connecting.cursor(prepared=True) as cursor:
                    cursor.execute(query, (_id,))
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(e)
