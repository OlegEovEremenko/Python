# Практическое задание. Задача № 3

for percent in range(1, 101):
    if percent % 10 == 1:
        print(f'{percent} процент')
    elif percent % 10 == 2 or percent % 10 == 3 or percent % 10 == 4:
        print(f'{percent} процента')
    else:
        print(f'{percent} процентов')
