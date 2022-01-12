class Czlowiek:
    def __init__(self, imie: str, nazwisko: str, wiek: int, plec: str):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__wiek = wiek
        self.__plec = plec

    @property
    def imie(self):
        return self.__imie

    @property
    def nazwisko(self):
        return self.__nazwisko

    @property
    def wiek(self):
        self.__wiek

    @property
    def plec(self):
        return self.__plec

    def __str__(self) -> str:
        return f'Imie: {self.imie}, nazwisko: {self.nazwisko}, wiek: {self.wiek}, płeć: {self.plec}'
