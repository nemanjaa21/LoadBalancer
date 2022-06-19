from mysql.connector import connect, Error


class AnaliticsReport:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def potrosnja_po_gradu(self, *args):
        if len(args) > 1:
            return -5
        _grad = args[0]
        try:
            with connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
            ) as connecting:
                query = """SELECT pb.IdBrojila, Mesec, Potrosnja FROM brojilo p, potrosnjaBrojila pb 
                           WHERE p.IdBrojila = pb.IdBrojila and Grad = (?) ORDER BY pb.IdBrojila, Mesec;"""
                with connecting.cursor(prepared=True) as cursor:
                    cursor.execute(query, (_grad,))
                    result = cursor.fetchall()
                    return result
        except Error as e:
            return e

    def potrosnja_po_brojilu(self, *args):
        if len(args) > 1:
            return -5
        _id = args[0]
        try:
            with connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
            ) as connecting:
                query = """SELECT Mesec, Potrosnja FROM potrosnjaBrojila 
                           WHERE IdBrojila = (?) ORDER BY Mesec;"""
                with connecting.cursor(prepared=True) as cursor:
                    cursor.execute(query, (_id,))
                    result = cursor.fetchall()
                    return result
        except Error as e:
            return e
