def testFactorial(a):
    x = 0
    i = 1
    while i <= a:
        if i % 2 == 0:
            x += i
        i += 1
    return x


num = int(input("Введите число: "))

result = testFactorial(num)
print("Сумма всех четных чисел от 1 до", num, "включительно равна:", result)
