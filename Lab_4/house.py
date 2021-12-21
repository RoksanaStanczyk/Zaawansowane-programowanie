from property import Property


class House(Property):
    def __init__(self, area: float, rooms: int, plot: int):
        super().__init__(self, area, rooms)
        self.__plot = plot

    def __str__(self):
        return Property.__str__() +  ' plot: {self.plot}'
