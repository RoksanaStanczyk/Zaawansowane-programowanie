from dieta import Dieta
from pacjent import Pacjent
from dietetyk import Dietetyk
from zamowienie import Zamowienie

dieta = Dieta(1000, 'mięsna', '10', 2000)
dieta2 = Dieta(1500, 'wege', '20', 2000)
pacjent = Pacjent('Adam', 'Nowak', 18, 'male', dieta)
dietetyk = Dietetyk('Michał', 'Kowalski', 55, 'male', pacjent)
zamowienie = Zamowienie()
zamowienie.dieta = [dieta, dieta2]
zamowienie.pacjent = pacjent
print(zamowienie)
print(zamowienie.wartosc())
print(zamowienie.kcal_all())
