'''
Склонение слова
Реализовать склонение слова «процент» во фразе «N процентов».
Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов
'''

def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    # место для Вашего кода
    result = ''
    remainder = number % 10
    if number == 1 or remainder == 1:
        result = str(number) + ' процент'
    elif (n > 1 and n < 5) or (n > 20 and (remainder > 1 and remainder < 5)):
        result = str(number) + ' процент' + 'а'
    else:
        result = str(number) + ' процент' + 'ов'
    return result

if __name__ == '__main__':
    for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
        print(transform_string(n))
