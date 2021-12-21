class Employee:
    def __init__(self, first_name: str, last_name: str):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__first_name


    @first_name.setter
    def first_name(self, first_name: str):
        self.__first_name = first_name


    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self.__last_name = last_name

    def __str__(self) -> str:
        return f'Imię pracownika to: {self.first_name}, a nazwisko: {self.last_name}'
