# 1


def introduce(name, surname):
    x = (f"Cześć {name} {surname}!")
    return x


zmienna_1 = introduce("Roksana", "Stanczyk")
print(zmienna_1)

# 2


def multiplication(a, b):
    return a * b


multiplication(2, 2)

# 3


def num(a):
    if a % 2 is 0:
        return True
    else:
        return False


zmienna = num(1)
if zmienna is True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

# 4


def compare_num(a, b, c):
    if a + b >= c:
        return True
    else:
        return False


compare_num(1, 2, 3)

# 5


def check(num_list, num):
    if num is num_list:
        print(True)
    else:
        print(False)


check([1, 2, 3, 4, 5], 6)

# 6
list3 = []


def list(list1, list2):
    list3 = set(list1 + list2)
    list3 = [i ** 3 for i in list3]
    print(list3)


list([1, 2], [2, 3])
