def decorator(url):
    print('Первый вызов и передача параметра в декоратор', url)

    def wrapper1(func):
        print('Вызов декоратора')

        def wrapper2(*args, **kwargs):
            print('Вызов функции внутри декоратора')
            res = func(*args, **kwargs)
            print('result')
            return res

        return wrapper2

    return wrapper1


@decorator(url='sdcsdc')
def some_func(arg):
    for i in range(3):
        print(i, 'some func', arg)


some_func('sdvsd')
