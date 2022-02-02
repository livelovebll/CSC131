a = [1, 2, 4, 1, 5, 6, 7, 8, 9, 10]
b = [2, 1, 5, 3, 6, 0, 55, 9, 10]

c = []

for number in a:
    if number in b:
        if number not in c:
            c.append(number)

print(c)