"""
Создайте классы утка и человек. У обоих классов нету свойств, но есть методы крякать и носить одежду.
Утка крякает, а человек имитирует кряканье. Добавьте экземпляры этих классов в список и вызовите в цикле соответствующие методы.
"""

class Duck:
    def wears(self):
        print('wears feathers')
    def make_sound(self):
        print('Crya')

class Human:
    def wears(self):
        print('wears clothes')

    def make_sound(self):
        print('Crya-crya')