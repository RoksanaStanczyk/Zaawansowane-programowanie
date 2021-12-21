from book import Book
from employee import Employee
from library import Library
from order import Order
from student import Student
from property import Property
from house import House
from flat import Flat

library = Library('Gliwice', 'Orzechowa')
employee = Employee('Adam', 'Kędzior')
student = Student('Kasia', 0)
book = Book(library, '2021-12-20')
order = Order(employee, student, book)
# print(order)

property = Property(345, 2)
# property = Property(39, 3)
# property.__str__()
house = House(58.5, 4, 244)
flat = Flat(100, 5, 100)
