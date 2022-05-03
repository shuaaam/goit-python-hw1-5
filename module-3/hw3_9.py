'''Для функции из предыдущей задачи создайте строки документации. Можно использовать следующий шаблон

    """Функция возвращает общую сумму доставки.
    Первый параметр &mdash; количество товаров в заказе.
    Параметр скидки discount, передаваемый только по ключу, по умолчанию имеет значение 0."""'''


def cost_delivery(quantity, *_, discount=0):
    """Функция возвращает общую сумму доставки.
    Первый параметр &mdash; количество товаров в заказе.
    Параметр скидки discount, передаваемый только по ключу, по умолчанию имеет значение 0."""

    result = (5 + 2 * (quantity - 1)) * (1 - discount)
    return result


print(cost_delivery.__doc__)
