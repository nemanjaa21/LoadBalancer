from mysql.connector import connect, Error


def get_brojilo(id):
    try:
        with connect(
                host='127.0.0.1',
                user='admin',
                password='admin',
                database='RES_PROJEKAT'
        ) as connecting:
        #TO DO
    except Error as e:
        print(e)


def get_potrosnja_brojila(id, mesec):
    try:
        with connect(
                host='127.0.0.1',
                user='admin',
                password='admin',
                database='RES_PROJEKAT'
        ) as connecting:
        #TO DO
    except Error as e:
        print(e)


def insert(id, mesec, potrosnja):
    try:
        with connect(
                host='127.0.0.1',
                user='admin',
                password='admin',
                database='RES_PROJEKAT'
        ) as connecting:
        #TO DO
    except Error as e:
        print(e)