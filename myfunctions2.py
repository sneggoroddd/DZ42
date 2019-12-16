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
