# Практическое задание. Задача № 1

duration = int(input('Введите временной отрезок в секундах: '))

if duration < 60:
    print(f'{duration} сек')

elif 60 <= duration < 3600:
    m = duration // 60
    s = duration % 60
    print(f'{m} мин {s} сек')

elif 3600 <= duration < (3600 * 24):
    h = duration // 3600
    m = duration % 3600 // 60
    s = duration % 60
    print(f'{h} час {m} мин {s} сек')

else:
    d = duration // (3600 * 24)
    h = duration % (3600 * 24) // 3600
    m = duration % 3600 // 60
    s = duration % 60
    print(f'{d} дн {h} час {m} мин {s} сек')
