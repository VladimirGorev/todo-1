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


class Calculator:

    def __init__(self, num):
        self.num = num
        self.buffer = []

    def plus(self, value):
        self.buffer.append(
            ('plus', value)
        )
        return self

    def minus(self, value):
        self.buffer.append(
            ('minus', value)
        )
        return self

    def calc(self):
        for oper, value in self.buffer:
            if oper == 'plus':
                self.num += value
            if oper == 'minus':
                self.num -= value
        return self.num

obj = Calculator(10)
print(obj.plus(5).minus(5).plus(3).minus(4).calc())
