
class DecoratorClass:

    def __init__(self, url):
        print('первый вызов DecoratorClass и передача параметра')
        self.url = url
        self.func = None

    def __call__(self, *args, **kwargs):
        if self.func is None:
            print('второй вызов DecoratorClass и передача функции в декоратор')
            self.func = args[0]
            return self
        else:
            print('вызов функции внутри DecoratorClass и передача аргументов в функцию')
            return self.func(*args, **kwargs)


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


@DecoratorClass(url='class_url')
def some_func(arg):
    for i in range(3):
        print(i, 'some func', arg)


some_func('sdvsd')
