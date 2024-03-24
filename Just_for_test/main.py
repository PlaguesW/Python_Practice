qty = int(input())
numbers = []
function = []
for i in range(1, qty + 1):
    num = int(input())
    numbers.append(num)
    f = num * num + 2 * num + 1
    function.append(f)
print(*numbers, sep='\n')
print()
print(*function, sep='\n')

qty = int(input())
words = []
for i in range(qty):
    word = input()
    if i not in words:
        words.append(i)
        print(i)

qty = [input() for x in range(int(input()))]
name = input().lower()
for i in qty:
    if name in i.lower():
        print(i)

s = [input() for _ in range(int(input()))]
d = [input() for _ in range(int(input()))]
for i in s:
    for j in d:
        if j.lower() not in i.lower():
            break
    else:
        print(i)

n = int(input())
x = [int(input()) for _ in range(n)]
[print(i) for i in x if i < 0]
[print(i) for i in x if i == 0]
[print(i) for i in x if i > 0]

s = '192.168.0.3'
s = s.split('.')
for i in s:
    if int(i) < 0 or int(i) > 255:
        print('НЕТ')
        break
else:
     print('ДА')

a = input().split()
count = 0
for i in range(len(a) - 1):
    count += a[i + 1:].count(a[i])
print(count)

text = input()
for i in range(int(text[1:])):
    s = input()
    if '#' in s:
        s = s[:s.find('#')]
    print(s.rstrip())

num = input().split()
for i in range(len(num)):
    num[i] = int(num[i])
num.sort()
print(*num)
num.sort(reverse=True)
print(*num)

num = 5
print(*[i ** 2 for i in range(1, num + 1)], sep='\n')

phrase = 'Умей ценить того кто без тебя не может'
print(*phrase.split(), sep='\n')

for a in range(1, 33):
    for c in range(1, a):
        for d in range(1, c):
            for b in range(1, d):
                if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                    print(a**3 + b**3)
sleep_min = 475
go_bed_h = 1
go_bed_m = 55
alarm_h = (go_bed_h * 60 + sleep_min) / 60
alarm_m = (sleep_min + go_bed_h * 60 + go_bed_m) % 60
print(round(alarm_h), alarm_m, sep='\n')

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

operations = {
      "+": lambda x, y: x + y,
      "-": lambda x, y: x - y,
      "/": lambda x, y: x / y,
      "*": lambda x, y: x * y,
      "mod": lambda x, y: x % y,
      "pow": lambda x, y: x ** y,
      "div": lambda x, y: x // y
}

x, y = float(input()), float(input())
operation = input()

if operation in ["mod", "div", "/"] and y == 0:
    print("Деление на 0!")
else:
    print(operations[operation](x, y))

a, b, c = 1, 2, 3
numbers = []
numbers.append(a)
numbers.append(b)
numbers.append(c)
numbers = numbers.sort()
print(numbers)

a =int (input())
b =int (input())
c =int (input())
d =int (input())
for g in range (c,d+1):
    print('\t'+str(g),end='')
print(end='\n')
for i in range (a,b+1):
    print(str(i)+'\t',end='')
    for j in range (c,d+1):
        print(str(i*j),end='\t')
    print(end='\n')

a, b, c, d = int(input()), int(input()), int(input()), int(input())
for i in range(c, d + 1):
    print('\t' + str(i), end='')
print(end='\n')
for j in range(a, b + 1):
    print(str(j) + '\t', end='')
    for k in range(c, d + 1):
        print(str(i*j), end='\t')
    print(end='\n')

letters = 'acggtgttat'
letter_c = letters.upper().count('C')
letter_g = letters.upper().count('G')
summ = letter_c + letter_g
print((summ / len(letters)) * 100)

dna = 'aaaabbcdcb'
lenght = len(dna)
count = 1
for i in range(lenght):
    if i == (lenght - 1):
        print(dna[i] + str(count), end='')
    else:
        if dna[i] == dna[i + 1]:
            count = count + 1
        else:
            print(dna[i] + str(count), end='')
            count = 1

num = [int(i) for i in input().split()]
res = 0
lenght = len(num) - 1
for i in range(0, lenght + 1):
    res += num[i]
print(res)

numbers = input().split()
if len(numbers) == 1:
    print(numbers[0])
elif len(numbers) > 1:
    summ = [int(numbers[i - 1]) + int(numbers[i + 1]) for i in range (-1, len(numbers) - 1)]
    for i in range (1, len(summ)):
        print(summ[i], end=' ')
    print(summ[0])

num = [int(i) for i in input().split()]
num.sort()
count = []
for i in range(1, len(num)):
    if num[i] == num[i - 1]:
        if num[i] not in count:
            count.append(num[i])
for i in range(0, len(count)):
    print(count[i], end =' ')


num = int(input())
total = num
sqr = 0 + abs(num ** 2)
while total != 0:
    num = int(input())
    total = total + num
    sqr = sqr + abs(num) ** 2
    if total == 0:
        break
print(sqr)

s=[int(input())]
while sum(s)!=0: #s.append(int(input()))
print(sum([i**2 for i in s]))

num_input = 7
seq = []
num = 1
for i in range(1, num_input + 1):
    for j in range(i):
        if len(seq) < num_input:
            seq.append(str(num))
        else:
            break
    num += 1
print(' '.join(seq))

numbers = [int(i) for i in input().split()]
num = int(input())

for i in range(len(numbers)):
    if num == numbers[i]:
        print(i, end=' ')

if num not in numbers:
    print('Отсутствует')

row = ''
matrix = []
while True:
    row = input()
    if row == 'end':
        break
    matrix.append([int(i) for i in row.split()])
ai = len(matrix)
aj = len(matrix[0])
newMatrix = [
    [(matrix[i - 1][j] + matrix[(i + 1) % ai][j] + matrix[i][j - 1] + matrix[i][(j + 1) % aj])
     for j in range(aj)]
    for i in range(ai)]
for i in range(ai):
    for j in range(aj):
        print(newMatrix[i][j], end=' ')
    print()


num = int(input())
x = 0
y = 0
dx = 1
dy = 0
matrix = [[None] * num for _ in range(num)]
for i in range(1, num ** 2 + 1):
    matrix[x][y] = i
    nx = x + dx
    ny = y + dy
    if (0 <= nx < num) and (0 <= ny < num) and (not matrix[nx][ny]):
        x = nx
        y = ny
    else:
        swap = -dy
        dy = dx
        dx = swap
        x = x + dx
        y = y + dy
for y in range(num):
    for x in range(num):
        print(matrix[x][y], end = ' ')
    print()


num = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78,
96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6,
52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44,
25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56,
-41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19,
-13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38,
-55, 7, -11, -26, -62, -84]
list = len(num)
for i in range(list - 1):
    check = True
    for j in range(list - i - 1):
        if num[j] >= num[j + 1]:
            check = False
            num[j], num[j + 1] = num[j + 1], num[j]
    if check == True:
        break

print('Список по возрастанию: ', num)

n = len(a)
for i in range(n - 1):
    b = a[i:].index(min(a[i:]))
    a[i], a[b + i] = a[b + i], a[i]
print(a)

insert sort
numbers = [1, 45, -34, 34, 54, 446, 930, 560, -1, 0, 12, 34, 34]
list = len(numbers)
for i in range(1, list):
    elem = numbers[i]
    j = i
    while j >= 1 and numbers[j - 1] > elem:
        numbers[j] = numbers[j - 1]
        j -= 1
    numbers[j] = elem
print('Отсвортированный список:', numbers)

def draw_box():
    print('*' * 10)
    for i in range(12):
        print('*' + ' ' * 8 + '*')
    print('*' * 10)

draw_box()

with open('dataset_3363_2.txt') as t:
    s = t.readline().strip()
def rep(symbol, iter): return symbol*int(iter)
i = 0
while i < len(s):
    iter = ''
    if s[i].isalpha():
        symbol = s[i]
        i += 1
        while s[i].isdigit():
            iter += s[i]
            if i == len(s)-1: break
            i += 1
        print(rep(symbol, iter),end='')

with open('dataset_3363_3.txt') as inf, open('MostPopularWord.txt','w') as ouf:
    maxc = 0
    s = inf.read().lower().strip().split()
    s.sort()
    for word in s:
        counter = s.count(word)
        if counter > maxc:
            maxc = counter
            result_word = word
    ouf.write(result_word +' ' + str(maxc))

math_values = []
physics_values = []
russian_values = []
with open('dataset_3363_4.txt', 'r') as in_file:
    for line in in_file:
        current_line = line.strip().split(';')
        math_values.append(int(current_line[1]))
        physics_values.append(int(current_line[2]))
        russian_values.append(int(current_line[3]))
out_file = open('statistic.txt', 'w')
for i in range(len(math_values)):
    out_file.write(str((math_values[i] + physics_values[i] + russian_values[i]) / 3) + '\n')
if len(math_values) > 0:
    out_file.write(str(sum(math_values) / len(math_values)) + ' ' +
                   str(sum(physics_values) / len(physics_values)) + ' ' +
                   str(sum(russian_values) / len(russian_values)))
out_file.close()

import sys
s = ''
s2 = ''
for i in range(1,len(sys.argv)):
    s = s + sys.argv[i]+' '
s2 = s
print(s2,end=' ')

def draw_box(height, width):
    for i in range(height):
        print('*' * width)
draw_box(5, 7)

def print_number(a, b, c):
    d = (a + c) // b
    print(d)
print_number(2, 3, 11)

def draw_triangle(fill, base):
    for i in range(1, base + 1):
        print(fill * min(i, base - i + 1))
fill, base = input(), int(input())
draw_triangle(fill, base)

temp = 60
def convert_to_celsius(temp):
    result = (5/9) * (temp - 32)
    return result
celsius = convert_to_celsius(temp)
print(celsius)


def get_days(month):
    if month == 2:
        return 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30

num = 1

print(get_days(num))

def get_factors(num):
    return [n for n in range(1, num + 1) if num % n == 0]

n = 15

print(get_factors(n))

list_1 = [1, 4, 67, 34, 67, 23, 67, 88, 90]
list_2 = [44, 23, 65, 23, 67, 99]
def merge(list_1, list_2):
    result = list_1 + list_2
    result.sort()
    return result
print(merge(list_1, list_2))


n = int(input())
def quick_merge(n):
    return sorted([int(i) for i in range(n) for i in input().split()])
print(*quick_merge(n))

name = 'abch12345h'
print(name[:name.find('h')] + name[name.rfind('h'):name.find('h'):-1] + name[name.rfind('h'):])


num = 15
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

if is_even(num):
    print('Число четное')
else:
    print('Число нечетное')


def is_valid_triangle(side1, side2, side3):
    if a < b+c and b < a+c and c < a+b:
        return True
    else:
        return False

a, b, c = 2, 2, 10

print(is_valid_triangle(a, b, c))


def get_next_prime(num):
    num += 1
    for i in range(2, num):
        if num % i == 0:
            return get_next_prime(num)
    return num

n = 1

print(get_next_prime(n))


def is_password_good(password):
    upp = [i for i in password if i.isupper()]
    low = [i for i in password if i.islower()]
    dig = [i for i in password if i.isdigit()]
    return all([len(password) >= 8, upp, low, dig])

txt = 'vhsdhvH3'

print(is_password_good(txt))


def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False

txt1 = 'aanb'
txt2 = 'bnat'

print(is_one_away(txt1, txt2))


def is_palindrome(text):
    for i in '.,!-? ':
        text = text.replace(i, '')
    return text.lower() == text[::-1].lower()

txt = input()

print(is_palindrome(txt))


def isPalindrom(n):
    n = str(n)
    return(n == n[::-1])

def isPrime(n):
    if n % 2 == 0: return(n == 2)
    d = 3
    while d * d <= n and n % d != 0: d += 2
    return(d * d > n)

def isEven(n): return(not n % 2)

def is_valid_password(password):
    try:
        a, b, c = map(int, password.split(':'))
        return(isPalindrom(a) and isPrime(b) and isEven(c))
    except: return(False)

psw = '1221:101:22'

print(is_valid_password(psw))


def convert_to_python_case(str, sep='_'):
    snake_register = ''
    for i in str:
        if i.isupper():
            snake_register += sep + i.lower()
        else:
            snake_register += i
    return snake_register.lstrip(sep)

txt = input()

print(convert_to_python_case(txt))


def get_middle_point(x1, y1, x2, y2):
    return (x1 + x2) / 2, (y1 + y2) / 2

x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)


import math
def get_circle(radius):
    return 2 * math.pi * radius, math.pi * radius ** 2

# считываем данные
r = 1

# вызываем функцию
length, square = get_circle(r)
print(length, square)


# объявление функции
def solve(a, b, c):
    d = b**2-4*a*c
    x1 = (-b - d ** 0.5) / (2*a)
    x2 = (-b + d ** 0.5) / (2*a)
    return min(x1, x2), max(x1, x2)

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)


import random

num = random.randrange(1, 100)
print(num)


import random

again = 'д'
while again.lower() == 'д':
    print('Бросаем кубики... ')
    print('Значения граней:')
    print(random.randint(1, 6))
    print(random.randint(1, 6))
    again = input('Бросить кубики еще раз? (д = да, н = нет): ')


import random

for _ in range(10):
    num = random.randint(0, 1)
    if num == 0:
        print('Орел')
    else:
        print('Решка')


num = 8
even_list = []
for i in range(2, num + 1, 2):
    even_list.append(i)
print(even_list)


numbers = 2, 5, 11, 33, 55
print(*numbers, sep='+', end='=')
print(sum(numbers))


n = input().split("-")
c = [len(i) for i in n]
if c == [3, 3, 4] and ''.join(n).isdigit():
    print("YES")
elif c == [1, 3, 3, 4] and ''.join(n).isdigit() and n[0] == '7':
    print("YES")
else:
    print("NO")


text = 'Привет    !'
rub = len(text) * 0.6
cent = len(text) * 60 % 100
print(f'{int(rub)} р. {cent} коп.')


year = 1989
zodiac = ['Обезьяна','Петух','Собака','Свинья','Крыса','Бык','Тигр','Заяц','Дракон','Змея','Лошадь','Овца']
print(zodiac[year % 12])


n = int(input())
k = int(input())

res = 0
for i in range(1, n + 1):
    res = (res + k) % i
print(res + 1)


number = int(input())
first, second, third, fourth = 0, 0, 0, 0

for i in range(number):
    x, y = map(int, input().split())
    first += x > 0 and y > 0
    second += x < 0 and y > 0
    third += x < 0 and y < 0
    fourth += x > 0 and y < 0

print(f"Первая четверть: {first}")
print(f"Вторая четверть: {second}")
print(f"Третья четверть: {third}")
print(f"Четвертая четверть: {fourth}")


numbers = [int(n) for n in input().split()]
count = 0
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        count += 1
print(count)


nums = [int(i) for i in input().split()]
for i in range(0, len(nums) - 1, 2):
    nums[i], nums[i + 1] = nums[i + 1], nums[i]
print(*nums)


n = list(map(int, input().split()))
n.insert(0, n[-1])
del n[-1]
print(*n)


print(len(set(input().split())))


Timur = input().lower()
Ruslan = input().lower()
if Timur == 'камень' and Ruslan == 'ножницы' or  Timur == 'ножницы' and Ruslan == 'бумага' or Timur == 'бумага' and Ruslan == 'камень':
    print('Тимур')
elif Timur == Ruslan:
    print('ничья')
else:
    print('Руслан')
rus = input()
tim = input()

def game_3(ruslan, timur):
    x = ['камень', 'ножницы', 'бумага']
    y = ['0', '1', '2']
    ruslan = int(y[x.index(ruslan)])
    timur = int(y[x.index(timur)])
    if ruslan == timur:
        return('ничья')
    elif ruslan > timur and (timur + 1) % 3 == ruslan or timur > ruslan and (ruslan + 1) % 3 != timur:
        return('Руслан')
    else:
        return('Тимур')

print(game_3(rus, tim))


Timur = input().lower()
Ruslan = input().lower()
if Timur == 'камень' and Ruslan == 'ножницы' or  Timur == 'ножницы' and Ruslan == 'бумага'\
        or Timur == 'бумага' and Ruslan == 'камень' or Timur == 'камень' and Ruslan == 'ящерица'\
        or Timur == 'спок' and Ruslan == 'ножницы' or Timur == 'ящерица' and Ruslan == 'спок'\
        or Timur == 'ножницы' and Ruslan == 'ящерица' or Timur == 'ящерица' and Ruslan == 'бумага'\
        or Timur == 'бумага' and Ruslan == 'спок' or Timur == 'спок' and Ruslan == 'камень':
    print('Тимур')
elif Timur == Ruslan:
    print('ничья')
else:
    print('Руслан')
def product():

    characters = dict()
    characters["Камень"] = ["Ящерица", "Ножницы"]
    characters["Ножницы"] = ["Бумага", "Ящерица"]
    characters["Бумага"] = ["Камень", "Спок"]
    characters["Ящерица"] = ["Спок", "Бумага"]
    characters["Спок"] = ["Ножницы", "Камень"]

    timur_move = input().title()
    ruslan_move = input().title()

    if timur_move == ruslan_move:
        return "ничья"
    elif ruslan_move in characters[timur_move]:
        return "Тимур"
    else:
        return "Руслан"
print(product())


virus = 'anton'

for i in range(1, int(input()) + 1):
    s, res = input(), ''
    for j in virus:
        if j in s:
            res += j
            s = s[s.find(j):]

    if res == 'anton':
        print(i, end=' ')
        continue


for i in range(int(input())):
    s, virus, x  = input(), 'anton', 0
    for sym in s:
        if sym == virus[x]:
            x += 1
        if x == 5:
            print(i + 1, end=' ')
            break



word = input() + ' запретил букву'
alpha = [chr(i) for i in range(1072, 1104)]

for letter in alpha:
    if letter in word:
        print(word, letter)
        word = word.replace(letter, '').replace('  ', ' ').strip()


name = ['pojd', 'ubns', 'index']
print (name)
name.sort()
print(name)
name.pop(1)
print(name)
del name[0]
print(name)

# объявление функции
def func(num1, num2):
    if num1 % num2 == 0:
        return True

# считываем данные
num1, num2 = int(input()), int(input())

# вызываем функцию
if func(num1, num2):
    print('делится')
else:
    print('не делится')
print(10 / 1000)


letters = ['a', 'b', 'c', 'd']
new_letters = list(letters)
print(new_letters)
# new_letters = new_letters.copy(letters)
# print(new_letters)
new_letters = letters[:]
print(new_letters)
new_letters = letters.copy()
print(new_letters)
# new_letters = copy(letters)
# print(new_letters)


for i in input():
    if i.isalpha():
        print(chr((ord(i) + 10) % ord('я')), end='')
    else:
        print(i, end='')


my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

maximum = my_list[0][0]
minimum = my_list[0][0]

for row in my_list:
    if max(row) > maximum:
        maximum = max(row)
    if min(row) < minimum:
        minimum = min(row)

print(maximum + minimum)


num = int(input())
matrix = [[j for j in range(1, num + 1)] for i in range(1, num + 1)]
print(*matrix, sep='\n')

n = int(input())
matrix = [[j for j in range(1, i + 1)] for i in range(1, n + 1)]
print(*matrix, sep='\n')

n = int(input())
s = []
for i in range(n+1):
    row=[1]*(i+1)
    for j in range(i+1):
        if j!=i and j!=0: row[j] = s[i-1][j-1]+s[i-1][j]
    s.append(row)
print(s[n] if n!=0 else [1])


n = int(input())
P=[]
for i in range(0,n):
    row=[1]*(i+1)
    for j in range(i+1):
        if j!=0 and j!=i:
            row[j]=P[i-1][j-1]+P[i-1][j]
    P.append(row)

for r in P:
    print(*r)


res = []

for i in input().split():
    if res and i in res[-1]:
        res[-1].append(i)
    else:
        res.append([i])

print(res)


def chunked(st, n):
    st = st.split()
    a = [[] for _ in range(0, len(st), n)]
    for i in range(len(a)):
        a[i].extend(st[:n])
        st = st[n:]
    return a

string = input()
num = int(input())

print(chunked(string, num))


n=input().split()
o=[[]]
k=1
while k!=len(n)+1:
    for j in range(len(n)):
        if len(n[j:j+k])==k:
            o.append(n[j:j+k])
    k+=1
print (o)


rows, cols = 4, 4
matrix = [[100, 2, 30, 415],
          [57, 6, 79, 8934],
          [94, 10, 1123, 120],
          [13, 1434, 155, 1668]]

for r in range(rows):
    for c in range(cols):
        print(matrix[r][c], end=' ')
    print()

for c in range(cols):
    for r in range(rows):
        print(str(matrix[r][c]).ljust(4), end=' ')
    print()


n = 8
matrix = [[0]*n for _ in range(n)]# создаем квадратную матрицу размером 8×8

for i in range(n):# заполняем главную диагональ единицами, а побочную двойками
    matrix[i][i] = 1
    matrix[i][n-i-1] = 2

for r in range(n):# выводим матрицу
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()


n = 5
a = [[19, 21, 33, 78, 99],
     [41, 53, 66, 98, 76],
     [79, 80, 90, 60, 20],
     [33, 11, 45, 67, 90],
     [45, 67, 12, 98, 23]]

maximum = -1
minimum = 100

for i in range(n):
    if a[i][i] > maximum:
        maximum = a[i][i]
    if a[i][n - i - 1] < minimum:
        minimum = a[i][n - i - 1]
print(minimum + maximum)



m, n, matrix = int(input()), int(input()), []
for i in range(m):
    matrix.append([input() for _ in range(n)])
    print(*matrix[i])

res = 0
for i in range(int(input())):
    res += int(input().split()[i])
print(res)


n, m = int(input()), int(input())
def sum_mul(n, m):
    while n < m


name = input()
def remember (name):
    if len(name) < 2:
        return [name]
    else:
        return [name, name[0:2]]