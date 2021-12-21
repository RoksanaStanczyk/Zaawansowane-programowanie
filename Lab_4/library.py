class Library:
    def __init__(self, city: str, street: str):
        self.__city = city
        self.__street = street

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    def __str__(self) -> str:
        return f'Biblioteka znajduje się w mieście: {self.city}, na ulicy : {self.street}'
