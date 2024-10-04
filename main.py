sum = 0

while True:
    num = int(input("Введите число для сложения или 0 для выхода: "))
    if num == 0:
        break
    sum += num
print(sum)


b = [0, 1, 1]

while True:
    b.append(b[-1] + b[-2])
    if len(b) == 20:
        break
print(b)

str = input("Введите строку: ")
worms = str.split()
print(f"Количество слов: {len(worms)}")