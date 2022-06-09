from AnaliticsUI import AnaliticsUI


class DatabaseAnalitics:

    def __init__(self):
        self.menu = AnaliticsUI()
        self.do = True

    def Analitics_UI(self):
        while self.do:
            self.menu.Options()
            _input = input()
            self.do = self.menu.Handle(_input)


def main():
    databaseAnalitics = DatabaseAnalitics()
    databaseAnalitics.Analitics_UI()


if __name__ == "__main__":
    main()
