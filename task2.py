'''
Задание 2
* Создать список, состоящий из кубов нечётных чисел от 1 до 1000
  (куб X - третья степень числа X):
* Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. 
  Например, число «19 ^ 3 = 6859» будем включать в сумму,
  так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
* К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из 
  этого списка, сумма цифр которых делится нацело на 7. 
* Решить задачу под пунктом b, не создавая новый список.)
'''


def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    # место для написания кода
    total_sum_1 = 0
    for n in range(0, len(dataset)):
        sum_digits = 0
        check_number = dataset[n]
        while check_number >= 1:
            sum_digits += check_number % 10
            check_number = check_number // 10
        if sum_digits % 7 == 0:
            total_sum_1 += dataset[n]
    return total_sum_1
    # Верните значение полученной суммы


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка, 
        сумма цифр которых делится нацело на 7"""
    # место для написания кода
    total_sum_2 = 0
    for n in range(0, len(dataset)):
        sum_digits = 0
        check_number = dataset[n] + 17
        while check_number >= 1:
            sum_digits += check_number % 10
            check_number = check_number // 10
        if sum_digits % 7 == 0:
            total_sum_2 += (dataset[n] + 17)
    return total_sum_2
    # Верните значение полученной суммы


if __name__ == '__main__':
    my_list = []  # Соберите нужный список по заданию
    for i in range(0, 1001):
        my_list.append(i**3)
    # print(my_list)
    result_1 = sum_list_1(my_list)
    print(result_1)
    result_2 = sum_list_2(my_list)
    print(result_2)


