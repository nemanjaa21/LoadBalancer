from Projekat.DatabaseAnalitics.Classes.PotrosnjaGrad import PotrosnjaGrad
from Projekat.DatabaseAnalitics.Classes.PotrosnjaBrojila import PotrosnjaBrojila


class Parser:

    @staticmethod
    def parsiranje_po_gradovima(input_parameter):
        _ret_val = list()
        for _item in input_parameter:
            _report = PotrosnjaGrad(_item[0], _item[1], _item[2])
            _ret_val.append(_report)
        return _ret_val

    @staticmethod
    def parsiranje_po_brojilima(input_parameter):
        _ret_val = list()
        for _item in input_parameter:
            _report = PotrosnjaBrojila(_item[0], _item[1])
            _ret_val.append(_report)
        return _ret_val
