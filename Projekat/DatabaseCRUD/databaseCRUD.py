from Projekat.DatabaseCRUD.CRUDBrojila import CRUDBrojila
from Projekat.DatabaseCRUD.CRUDPotrosnjaBrojila import CrudPotrosnjaBrojila


class DatabaseCRUD:

    def __init__(self):
        self.crud_brojila = CRUDBrojila('127.0.0.1', 'admin', 'admin', 'RES_PROJEKAT')
        self.crud_potrosnja_brojila = CrudPotrosnjaBrojila('127.0.0.1', 'admin', 'admin', 'RES_PROJEKAT')

    def get_brojilo(self, id_param):
        return self.crud_brojila.read(id_param)

    def get_potrosnja_brojila(self, id_param, mesec_param):
        return self.crud_potrosnja_brojila.read(id_param, mesec_param)

    def insert(self, id_param, mesec_param, potrosnja_param):
        return self.crud_potrosnja_brojila.insert(id_param, mesec_param, potrosnja_param)
