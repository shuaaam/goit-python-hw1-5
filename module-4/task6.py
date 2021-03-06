"""
У нас есть список показателей студентов группы — это список с полученными балами по тестированию.
Необходимо список поделить на две части. Напишите функцию split_list, которая принимает список (целые числа),
находит среднее значение балла в списке и делит его на два списка. В первый попадают значения меньше среднего,
включая среднее значение, а во второй — строго больше среднего. Функция возвращает кортеж этих двух списков.
Для пустого списка возвращаем два пустых списка.
"""


def split_list(grade):
    under_num = []
    above_num = []

    if len(grade) != 0:
        middle_num = sum(grade) / len(grade)

        for n in grade:
            if n <= middle_num:
                under_num.append(n)
            else:
                above_num.append(n)
        return under_num, above_num

    else:
        return under_num, above_num
