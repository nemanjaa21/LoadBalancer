from Scripts.Parser import Parser
from Scripts.Report import Report
from Projekat.DatabaseCRUD.databaseCRUD import DatabaseCRUD


class AnaliticsUI:

    def __init__(self):
        self.db = DatabaseCRUD()

    def Options(self):
        print('1. Mesecna potrosnja brojila po gradovima')
        print('2. Mesecna potrosnja po brojilu')
        print('3. Izlaz')

    def Handle(self, option):
        _ret_val = True
        if option == '1':
            print("Grad: ")
            _grad = input()
            _result = self.db.get_potrosnja_po_gradu(_grad)
            _result = Parser.parsiranje_po_gradovima(_result)
            if _result:
                Report.prikazi_potrosnju_po_gradovima(_result)
            else:
                print("Ne postoji izvestaj za zadati grad!")
        elif option == '2':
            print("ID brojila: ")
            _id = input()
            _result = self.db.get_potrosnja_po_brojilu(_id)
            _result = Parser.parsiranje_po_brojilima(_result)
            if _result:
                Report.prikaz_potrosnje_po_brojilu(_result)
            else:
                print("Ne postoji izvestaj za zadato brojilo!")
        elif option == '3':
            _ret_val = False
        return _ret_val
