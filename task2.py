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
    # место для написания кода тут
    # создаю вспомогательный список из степеней числа 10, чтобы потом найти цифры в числах
    list_of_10 = [1]
    for i in range(1, 20):
        list_of_10.append(pow(10, i))
    list_of_10.reverse()

    # объявляем новые переменные
    sum_of_digit = 0
    total_sum = 0

    for i in my_list:
        remember_number = i # запоминаем текущие числа, так как дальше они будут меняться в цикле
        for j in list_of_10: # цикл для поиска суммы цифр в числе с использованием степеней числа 10
            # находим порядок числа (начиная с 100000000... и до сотни, десятка) и отделяем левую цифру делением нацело

            if i / j < 1:

                continue
            else:
                sum_of_digit += i // j
                i -= (i // j) * j

                continue

        if sum_of_digit % 7 == 0: # если сумма цифр делится на 7 без остатка, то добавляем число к общей сумме
            total_sum += remember_number
            sum_of_digit = 0
        sum_of_digit = 0 # обнуляем переменную для нового расчета следующего числа
    return total_sum  # Верните значение полученной суммы


def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    # место для написания кода
    list_of_10 = [1]
    for i in range(1, 20):
        list_of_10.append(pow(10, i))
    list_of_10.reverse()
    sum_of_digit = 0

    total_sum = 0

    for i in my_list:
        i += 17 # прибавляем ко всем числам из списка кубов +17
        remember_number = i
        for j in list_of_10:

            if i / j < 1:

                continue
            else:
                sum_of_digit += i // j
                i -= (i // j) * j

                continue

        if sum_of_digit % 7 == 0:
            total_sum += remember_number
            sum_of_digit = 0
        sum_of_digit = 0
    return total_sum  # Верните значение полученной суммы


if __name__ == '__main__':
    my_list = []  # Соберите нужный список по заданию
    for i in range (1,1000):
        if i%2 == 1:
            my_list.append(pow(i,3))
    print(my_list)
    result_1 = sum_list_1(my_list)
    print(result_1)
    result_2 = sum_list_2(my_list)
    print(result_2)