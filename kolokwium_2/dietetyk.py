from czlowiek import Czlowiek
from pacjent import Pacjent


class Dietetyk(Czlowiek):
    def __init__(self, imie: str, nazwisko: str, wiek: int, plec: str, pacjent: Pacjent):
        super().__init__(imie, nazwisko, wiek, plec)
        self.__pacjent = pacjent

    @property
    def pacjent(self):
        return self.__pacjent

    def __str__(self) -> str:
        return Czlowiek.__str__(self) + f'jego pacjentem jest: {self.pacjent}'
