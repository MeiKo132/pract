values = [input(f"введіть значення {i + 1}: ") for i in range(10)]
print("значення в зворотньому порядку:")
for value in reversed(values):
    print(value)