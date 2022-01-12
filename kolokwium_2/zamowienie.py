from dieta import Dieta
from pacjent import Pacjent


class Zamowienie:
    def __init__(self):
        self.__dieta = None
        self.__pacjent = None
        self.__wartosc = None
        self.__adres = None

    @property
    def dieta(self):
        return self.__dieta

    @dieta.setter
    def dieta(self, dieta: list):
        self.__dieta = dieta

    @property
    def pacjent(self):
        return self.__pacjent

    @pacjent.setter
    def pacjent(self, pacjent: Pacjent):
        self.__pacjent = pacjent

    @property
    def adres(self):
        return self.__adres

    @adres.setter
    def adres(self, adres: str):
        self.__adres = adres

    def __str__(self) -> str:
        return f'Zamówienie składa się z: {self.__dieta}, dla pacjenta: {self.__pacjent}, na adres: {self.__adres}' \
               f' cena diety: {self.wartosc()}'

    def wartosc(self) -> int:
        # return round(self.dieta.cena, 2)
        wartosc = 0
        for dieta in self.dieta:
            wartosc += dieta.cena
        return round(wartosc, 2)

    def kcal_all(self):
        kcal = 0
        for dieta in self.dieta:
            kcal += dieta.kaloryczność
        return round(kcal, 2)
