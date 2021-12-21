from employee import Employee
from student import Student
from book import Book


class Order:
    def __init__(self, employee: Employee, student: Student, book: Book):
        self.__employee = employee
        self.__student = student
        self.__book = book

    @property
    def employee(self):
        return self.__employee

    @employee.setter
    def employee(self, employee: Employee):
        self.__employee = employee

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, student: Student):
        self.__student = student

    @property
    def book(self):
        return self.__book

    @book.setter
    def book(self, book: Book):
        self.__book = book

    def __str__(self):
        return f'Pracownik: {self.employee}, student: {self.student}, książka: {self.book} '