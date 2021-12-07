# Практическое задание. Задача № 2

odd_number_cube = []

for number in range(1, 1000):
    if number % 2 != 0:
        cube = number ** 3
        odd_number_cube.append(cube)

# Часть a

our_list = []  # Список, куда будут помещены кубы с суммой цмфр кратной семи

for cube in odd_number_cube:  # Самым большим числом нашего списка является куб 999 - 997 002 999
    digit_1 = cube // 100_000_000  # Следовательно, чтобы получить первую цифру самых курпных чисел списка,
    digit_2 = cube // 10_000_000 % 10  # нужно использовать целочисленное деление на 100 000 000.
    digit_3 = cube // 1_000_000 % 10  # Если число маленькое, то целочисленное деление на крупное число даст ноль,
    digit_4 = cube // 100_000 % 10  # который не будет учитываться при подсчете суммы цифр.
    digit_5 = cube // 10_000 % 10
    digit_6 = cube // 1000 % 10
    digit_7 = cube // 100 % 10
    digit_8 = cube // 10 % 10
    digit_9 = cube % 10

    if (digit_1 + digit_2 + digit_3 + digit_4 + digit_5 + digit_6 + digit_7 + digit_8 + digit_9) % 7 == 0:
        our_list.append(cube)

result = sum(our_list)
print(f'Ответ на часть А: {result}')

# Часть b

our_new_list = []

for cube in odd_number_cube:
    cube += 17
    digit_1 = cube // 100_000_000
    digit_2 = cube // 10_000_000 % 10
    digit_3 = cube // 1_000_000 % 10
    digit_4 = cube // 100_000 % 10
    digit_5 = cube // 10_000 % 10
    digit_6 = cube // 1000 % 10
    digit_7 = cube // 100 % 10
    digit_8 = cube // 10 % 10
    digit_9 = cube % 10

    if (digit_1 + digit_2 + digit_3 + digit_4 + digit_5 + digit_6 + digit_7 + digit_8 + digit_9) % 7 == 0:
        our_new_list.append(cube)

result = sum(our_new_list)
print(f'Ответ на часть В: {result}')
