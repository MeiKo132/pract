values = [int(input(f"введіть значення {i + 1}: ")) for i in range(10)]

summ_parn = 0
summ_neparn = 0
numbers = set()
dublicat = set()
min_num = min(values)

for number in values:
    if number in numbers:
        dublicat.add(number)
    else:
        numbers.add(number)

for i in range(0, 10, 2):
    summ_neparn += values[i]
for i in range(1, 10, 2):
    summ_parn += values[i]
print(f"сумма парних елементів:{summ_parn}")
print(f"сумма не парних елементів:{summ_neparn}")
print(f"однакові значення:{dublicat}")
print(f"мінмальне значення:{min_num}")