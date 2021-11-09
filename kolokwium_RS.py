class Produkt:
    def __init__(self, waga, rodzaj, kolor, cena, id):
        self.__waga = waga
        self.__rodzaj = rodzaj
        self.__kolor = kolor
        self.__cena = cena
        self.__id = id

    @property
    def waga(self)->int:
        return self.__waga

    @property
    def rodzaj(self)->str:
        return self.__rodzaj

    @property
    def kolor(self)->str:
        return self.__kolor

    @property
    def cena(self):
        return self.__cena

    @property
    def id (self):
        return self.__id

    def __str__(self):
        return f'Produkt ma wagę: {self.waga} kg, jest to produkt z rodzaju {self.rodzaj}, ma kolor {self.kolor}, jego cena wynosi {self.cena}, jego id to {self.id}'

class KlientDetaliczny:
    def __init__(self, imie, nazwisko, nr_telefonu, miasto, adress):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__nr_telefonu = nr_telefonu
        self.__miasto = miasto
        self.__adress = adress

    @property
    def imie(self)-> str:
        return self.__imie

    @property
    def nazwisko (self)->str:
        return self.__nazwisko
    @property
    def nr_telefonu(self)-> str:
        return self.__nr_telefonu

    @property
    def miasto(self)->str:
        return self.__miasto

    @property
    def adress(self)-> str:
        return self.__adress

    def __str__(self):
        return f'imię i nazwisko klienta detalicznego to {self.imie},{self.nazwisko}, jego nr telefonu: /' \
               f'{self.nr_telefonu}, mieszka w mieście: {self.miasto}, pod adresem {self.adress}'


class KlientBiznesowy(KlientDetaliczny):
    def __init__(self, imie, nazwisko, nr_telefonu, miasto, adress):
        super().__init__(imie, nazwisko, nr_telefonu, miasto, adress)

    def __str__(self):
        return KlientDetaliczny.__str__(self)


class Magazyn:
    def __init__(self, liczba_produktow, miasto, adress, liczba_pracownikow, godziny_pracy):
        self.__liczba_produktow = liczba_produktow
        self.__miasto=miasto
        self.__adress = adress
        self.__liczba_pracownikow = liczba_pracownikow
        self.__godziny_pracy = godziny_pracy


    def __str__(self):
        return f'Magazyn posiada: {self.__liczba_pracownikow} pracownikow, jego siedziba znajduje się w mieście:' \
               f' {self. miasto}, pod adresem: {self.adress}, a pracownicy pracuja w godzinach {self.godziny_pracy}'

    @property
    def liczba_produktow(self)->int:
        return self.__liczba_produktow

    @property
    def miasto(self)-> str:
        return self.__miasto

    @property
    def adress(self) -> str:
        return self.__adress

    @property
    def liczba_pracownikow(self)->int:
        return self.__liczba_pracownikow

    @property
    def godziny_pracy(self) -> str:
        return self.__godziny_pracy


class Zamowienie:
    def __init__(self, produkt: Produkt, magazyn: Magazyn, klient_detaliczny: KlientDetaliczny, klient_biznesowy: KlientBiznesowy) :
        self.__produkt = produkt
        self.__magazyn = magazyn
        self.__klient_detaliczny = klient_detaliczny
        self.__klient_biznesowy = klient_biznesowy

    def __str__(self):
        return f'{self.produkt}, {self.__magazyn}, {self.__klient_detaliczny}, {self.__klient_biznesowy}'
    @property
    def produkt(self):
        return self.__produkt

    @produkt.setter
    def produkt(self, produkt: Produkt):
        self.produkt = produkt
        
        
pr = Produkt(3, 'elektryka', 'czarny', 50, 7)
m= Magazyn(10, 'Gliwice', 'zielona5', 40, '8-16')
k = KlientDetaliczny('Adam', 'Z', '4546', 'Katowice', 'Jerzebinowa 50')
klient_biznesowy = KlientBiznesowy('Jakub', 'Miara', '454554767', 'Gliwice', 'Kasztanowa 45')
#  print(klient_biznesowy)
z = Zamowienie(pr.__str__(), m.__str__(), k.__str__(), klient_biznesowy.__str__())
print(z)
    # def __init__(self, nazwa_towaru, ilosc_produktow, cena):
    #     self.__nazwa_towaru = nazwa_towaru
    #     self.__ilosc_produktow = ilosc_produktow
    #     self.__cena = cena
    #
    # def adres_klienta(self):
    #     return
    #
    # @property
    # def nazwa_towaru(self) -> str:
    #     return self.nazwa_towaru
    #
    # @nazwa_towaru.setter
    # def nazwa_towaru(self, nazwa_towaru: str):
    #     self.nazwa_towaru = nazwa_towaru
    #
    # @property
    # def ilosc_produktow(self) -> int:
    #     return self.ilosc_produktow
    #
    # @nazwa_towaru.setter
    # def ilosc_sztuk(self, ilosc_sztuk: int):
    #     self.ilosc_sztuk = ilosc_sztuk
    #
    # @property
    # def cena(self) -> int:
    #     return self.cena
    #
    # @nazwa_towaru.setter
    # def ilosc_sztuk(self, cena: int):
    #     self.cena = cena


