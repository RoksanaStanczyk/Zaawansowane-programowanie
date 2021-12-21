from library import Library


class Book:
    def __init__(self, library: Library, publication_date: str):
        self.__library = library
        self.__publication_date = publication_date

    @property
    def library(self):
        return self.__library

    @library.setter
    def library(self, library: Library):
        self.__library = library

    @property
    def publication_date(self):
        return self.__publication_date

    @publication_date.setter
    def publication_date(self, publication_date: str):
        self.__publication_date = publication_date

    def __str__(self) -> str:
        return f'Książka znajduje się w bibliotece {self.library} i została opublikowana {self.publication_date}'
