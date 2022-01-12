from czlowiek import Czlowiek
from dieta import Dieta

class Pacjent(Czlowiek):
    def __init__(self, imie: str, nazwisko: str, wiek: int, plec: str, dieta: Dieta):
        super().__init__(imie, nazwisko, wiek, plec)
        self.__dieta = dieta

    @property
    def dieta(self):
        return self.__dieta

    def __str__(self) -> str:
        return Czlowiek.__str__(self) + f'dieta: {self.dieta}'