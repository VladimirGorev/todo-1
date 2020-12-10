'''
Дескриптор это атрибут объекта со “связанным поведением”, то есть такой атрибут,
при доступе к которому его поведение переопределяется методом протокола дескриптора.
Эти методы  __get__, __set__ и __delete__.
Если хотя бы один из этих методов определен в объекте , то можно сказать что этот метод дескриптор.


Попробуем рассказать о дескрипторах чуть проще. В python существует три варианта доступа к атрибуту.
Допустим у нас есть атрибут a объекта obj:

Получим значение атрибута, some_variable = obj.a
Изменим его значение, obj.a = 'new value'
Удалим атрибут, del obj.a

Python позволяет перехватить выше упомянутые попытки доступа к атрибуту и переопределить
связанное с этим доступом поведение.
Это реализуется через механизм протокола дескрипторов.
'''


class AgeCheck:
    """
    Дескриптор
    """
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if value < 18:
            raise ValueError('Меньше 18 лет')
        instance.__dict__[self.name] = value


class Human:

    age = AgeCheck()

    def __init__(self, name, age):
        self.name = name
        self.age = age


man = Human('Bob', 20)
man.age = 15


