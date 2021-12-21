class Student:
    def __init__(self, name: str, marks: float):
        self.__name = name
        self.__marks = marks

    def is_passed(self):
        return self.__marks > 50

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def marks(self) -> float:
        return self.__marks

    @marks.setter
    def marks(self, marks: float):
        self.__marks = marks

    def __str__(self) -> str:
        return f'Imię: {self.name}, liczba_pkt: {self.marks}'
