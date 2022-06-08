from Projekat.DatabaseAnalitics.Classes.PotrosnjaBrojila import PotrosnjaBrojila


class PotrosnjaGrad(PotrosnjaBrojila):

    def __init__(self, id_parameter, mesec_parameter, potrosnja_parameter):
        self.id = id_parameter
        super().__init__(mesec_parameter, potrosnja_parameter)

    def get_id(self):
        return self.id
