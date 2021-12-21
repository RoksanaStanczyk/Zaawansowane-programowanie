class Property:
    def __init__(self, area: float, rooms: int):
        self.__area = area
        self.__rooms = rooms

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area: float):
        self.__area = area

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, rooms: int):
        self.__rooms = rooms

    def __str__(self) -> str:
        return f'Area: {self.__area}, rooms: {self.__rooms}'
