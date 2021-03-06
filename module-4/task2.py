"""
При анализе данных часто возникает необходимость избавиться от экстремальных значений,
прежде чем начать работать с данными дальше. Напишите функцию prepare_data, которая удаляет из
переданного списка наибольшее и наименьшее значение, сортирует его в порядке возрастания и
возвращает измененный список в качестве результата.
"""


def prepare_data(data):

    n = min(data)
    m = max(data)
    data.remove(n)
    data.remove(m)
    data_s = sorted(data)
    return data_s
