def simple_separator():
    return ('*'*10)
print(simple_separator() == '**********')  # True





def long_separator(count):
    return ('*' * count)
    """
    Функция создает разделитель из звездочек число которых можно регулировать параметром count
    :param count: количество звездочек
    :return: строка разделитель, примеры использования ниже
    """
print(long_separator(3) == '***')  # True
print(long_separator(4) == '****')  # True

def separator(simbol,count):
    return (simbol* count)

    """
    Функция создает разделитель из любых символов любого количества
    :param simbol: символ разделителя
    :param count: количество повторений
    :return: строка разделитель примеры использования ниже
    """
print(separator('-', 10) == '----------')  # True
print(separator('#', 5) == '#####')  # True



