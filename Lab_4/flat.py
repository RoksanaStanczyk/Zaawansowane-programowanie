from property import Property


class Flat(Property):
    def __init__(self, area: float, rooms: int, floor: int):
        super().__init__(self, area, rooms, floor)
        self.__floor = floor

    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self, floor: int):
        self.__floor = floor

    def __str__(self) -> str:
        return Property.__str__(self), f'floor: {self.floor}'