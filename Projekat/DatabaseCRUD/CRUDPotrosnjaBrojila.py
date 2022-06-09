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
                query = f"SELECT * FROM potrosnjaBrojila pb where pb.IdBrojila = %s and pb.Mesec = %s;"
                with connecting.cursor(prepared=True) as cursor:
                    parameter = (_id, _mesec)
                    cursor.execute(query, parameter)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            return e.errno


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
                query = f"INSERT INTO potrosnjaBrojila (IdBrojila, Potrosnja, Mesec) VALUES (?, ?, ?);"
                with connecting.cursor(prepared=True) as cursor:
                    parameter = (_id, _potrosnja, _mesec)
                    cursor.execute(query, parameter)
                    connecting.commit()
                    return cursor.rowcount
        except Error as e:
            return e.errno

    def delete(self, *args):
        pass

    def update(self, *args):
        pass