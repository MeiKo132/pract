import math


def disc(a, b, c):
    discr = b**2 - 4 * a * c

    if discr > 0:
        root1 = (-b + math.sqrt(discr)) / (a*2)
        root2 = (-b - math.sqrt(discr)) / (a * 2)
        return round(root1, 2), round(root2, 2)
    elif discr == 0:
        root = b / 2*a
        return round(root, 2)
    else:
        return "немає коренів"

a = float(input("уведіть коефіціент a: "))
b = float(input("уведіть коефіціент b: "))
c = float(input("уведіть коефіціент c: "))
result = disc(a, b, c)
print("корені рівняння -", result)