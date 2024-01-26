class Lada: #ниже пишем свойства указатели на экземпляр
    def __init__(self, model, color): #конструктор, init магический
        self.brand = 'Лада'
        self.model = model
        self.doors = 3.5
        self.color = color
        self.speed = 100
        self.broken_parts = 80

    def drive(self):
        print('Едем с кайфом')

    def barek(self):
        print('')

    def drift(self):
        print('дрифтим под твом окном в 3 ночи')

def some_func(some_object):
    print('Функция запустилась')
    some_object.drive()
    print('Метод отработал')

priora = Lada('приора', 'Чорни')
granta = Lada('гранта', 'баклажан')
print(granta.color)
some_func(granta)
granta.drive()

