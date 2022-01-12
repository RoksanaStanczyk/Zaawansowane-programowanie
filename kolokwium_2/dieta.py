class Dieta:
    def __init__(self, kaloryczność: int, rodzaj: str, okres_czasowy: str, cena: int):
        self.__kaloryczność = kaloryczność
        self.__rodzaj = rodzaj
        self.__okres_czasowy = okres_czasowy
        self.__cena = cena

    @property
    def kaloryczność(self):
        return self.__kaloryczność

    @property
    def rodzaj(self):
        return self.__rodzaj

    @property
    def okres_czasowy(self):
        return self.__okres_czasowy

    @property
    def cena(self):
        return self.__cena

    def __str__(self) -> str:
        return f'Kaloryczność diety wynosi: {self.kaloryczność}, jest to dieta {self.rodzaj}, na okres czasu: ' \
               f'{self.okres_czasowy} dni, cena wynosi: {self.cena}'
