"""
Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""


def naive_realisation(duration: int):
    total_time = ''
    """
    Решение задачи БЕЗ использования циклов.
    Переменная total_time - строковая переменная,
    содержащая в себе промежуток времени в нужно формате
    """

    # YOUR CODE HERE
    minute = 60
    hour = 60 * minute
    day = 24 * hour
    total_days = duration // day
    total_hours = (duration % day) // hour
    total_minutes = ((duration % day) % hour) // minute
    total_seconds = ((duration % day) % hour) % minute
    if total_days > 0:
        total_time = f'{total_days} дн. {total_hours} ч. {total_minutes} мин. {total_seconds} сек.'
    elif total_hours > 0:
        total_time = f'{total_hours} ч. {total_minutes} мин. {total_seconds} сек.'
    elif total_minutes > 0:
        total_time = f'{total_minutes} мин. {total_seconds} сек.'
    else:
        total_time = f'{total_seconds} сек.'
    return total_time


def one_cycle_realisation(duration):
    total_time = ''
    """
    Решение задачи с использования циклов.
    Можно два, но высший пилотаж через 1 цикл.
    Переменная total_time - строковая переменная,
    содержащая в себе промежуток времени в нужно формате
    """

    # YOUR CODE HERE

    minute = 60
    hour = 60 * minute
    day = 24 * hour
    total_seconds = 0
    total_minutes = 0  # 60
    total_hours = 0  # 3600
    total_days = 0 #86400

    while duration > 0:
        #print(f'{total_days} дн. {total_hours} ч. {total_minutes} мин. {total_seconds} сек.')
        if duration >= day:
            duration_day = duration // day
            total_days += duration_day
            duration = duration - total_days * day
            total_time += f'{total_days} дн. '
        elif duration % day >= hour:
            duration_hour = duration // hour
            total_hours += duration_hour
            duration = duration - total_hours * hour
            total_time += f'{total_hours} ч. '
        elif duration % hour >= minute:
            duration_minutes = duration // minute
            total_minutes += duration_minutes
            duration = duration - total_minutes * minute
            total_time += f'{total_minutes} мин. '
        else:
            total_seconds = duration
            total_time += f'{total_seconds} сек. '
            break
    return total_time


if __name__ == '__main__':
    duration = 628
    print(naive_realisation(duration))
    print(one_cycle_realisation(duration))
