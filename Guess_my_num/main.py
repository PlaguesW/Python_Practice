from random import randint
print('Добро пожаловать в числовую угадайку')
print()

# "Защита от дурака" при вводе числа пользователем
def is_valid(num):
    return num.isdigit() and 1 <= int(num)

# Угадайка числа с возможностью выбора правого интервала
def guess_the_number():
    print('Выберите уровень сложности.',
          'Чем больше интервал, из которого будет загадано искомое число, тем сложнее будет это искомое число отгадать.',
          'Итак, будет загадано число от 1 до ... (введите любое целое число больше 1)', sep='\n', end='\n')

    while True:    # Пользователь выбирает интервал, в котором будет загадано число
        n = input()
        if not is_valid(n):
            print('Нужно ввести целое число больше 1')
            continue
        break

    number = randint(1, int(n))    # Загадывается искомое число

    print(f'Введите целое число от 1 до {n}', end='\n')
    count = 0
    while True:    # Пользователь отгадывает число, ведется подсчет попыток
        digit = input()
        count += 1
        if not is_valid(digit) or int(digit) > int(n):
            print(f'А может быть все-таки введем целое число от 1 до {n}?')
            continue
        digit = int(digit)
        if digit > number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            continue
        elif digit < number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            continue
        else:
            print(f'Вы угадали, поздравляем! Количество попыток, за которое вам удалось угадать число: {count}')
            break


while True:
    guess_the_number()
    print('Хотите попробовать ещё раз? (да/нет)', end='\n')
    answer = input()
    while answer != 'да' and answer != 'нет':    # Проверка ответа (только "да" или "нет")
        print('Нужно ответить "да" или "нет"')
        answer = input()
    if answer == 'да':
        print('Отлично! Пробуем ещё раз!')
        print()
        continue
    elif answer == 'нет':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break