# Создайте класс имитирующий очередь LIFO

#метод push - добавление элемента в очередь
#Метод pop - достать из очереди


class Lifo:
    def __init__(self):
        self.query = []
    def push(self, val):
        self.query.insert(0,val)
    def pop(self):
        return self.query.pop(0)

bus = Lifo()
bus.push('Ann')
bus.push('Vanya')
bus.push('Vova')
print(bus.query)
