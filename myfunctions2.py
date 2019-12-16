def hello_world():
    return print('**********','\n','Hello World!','\n', '##########')



def hello_who(who='World'):
    return print('**********', '\n', 'Hello', {who} , '\n', '##########')
    """
    Функция печатает приветствие в красивом формате
    **********
    Hello {who}!
    ##########
    :param who: кого мы приветствуем, по умолчанию World
    :return: None
    """
hello_world()

hello_who("max")

def pow_many(power,  *args):
    summ = 0
    for arg in args:
        summ += arg
    return (summ**power)
    #Функция складывает любое количество цифр и возводит результат в степень power (примеры использования ниже)
    #:param power: степень
    #



print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100

