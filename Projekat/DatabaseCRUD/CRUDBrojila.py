from Projekat.DatabaseCRUD.CRUDAbstract import CRUD
from mysql.connector import connect, Error


class CRUDBrojila(CRUD):

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def insert(self, *args):
        _id = args[0]
        _ime = args[1]
        _prezime = args[2]
        _ulica = args[3]
        _broj = args[4]
        _postanskiBroj = args[5]
        _grad = args[6]

        try:
            with connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
            ) as connecting:
                query = """INSERT INTO brojilo (IdBrojila, Ime, Prezime, Ulica, Broj, PostanskiBroj, Grad) 
                                   VALUES (?, ?, ?, ?, ?, ?, ?);"""
                with connecting.cursor(prepared=True) as cursor:
                    parameter = (_id, _ime, _prezime, _ulica, _broj, _postanskiBroj, _grad)
                    cursor.execute(query, parameter)
                    connecting.commit()
                    return f"successfully inserted '{_id} {_ime} {_prezime} {_ulica} {_broj} {_postanskiBroj} {_grad}'"
        except Error as e:
            return e

    def delete(self, *args):
        _id = args[0]

        try:
            with connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
            ) as connecting:
                query = """DELETE FROM brojilo WHERE IdBrojila=(?)"""
                with connecting.cursor(prepared=True) as cursor:
                    parameter = (_id,)
                    cursor.execute(query, parameter)
                    connecting.commit()
                    return f"successfully deleted '{_id}'"
        except Error as e:
            print(e)

    def update(self, *args):
        _id = args[0]
        _ime = args[1]
        _prezime = args[2]
        _ulica = args[3]
        _broj = args[4]
        _postanskiBroj = args[5]
        _grad = args[6]

        try:
            with connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
            ) as connecting:
                query = """UPDATE brojilo SET Ime=(?), Prezime=(?), Ulica=(?), Broj=(?), PostanskiBroj=(?), Grad=(?)
                                   WHERE IdBrojila=(?);"""
                with connecting.cursor(prepared=True) as cursor:
                    parameter = (_ime, _prezime, _ulica, _broj, _postanskiBroj, _grad, _id)
                    cursor.execute(query, parameter)
                    connecting.commit()
                    return f"successfully updated '{_id} {_ime} {_prezime} {_ulica} {_broj} {_postanskiBroj} {_grad}'"
        except Error as e:
            print(e)

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
