a , b = [int(input("Введите число: ")) for _ in range(2)]
if a % b == 0:
    print("Да, делится")
else:
    print("Не делится, есть остаток", a % b)
print(a/b)