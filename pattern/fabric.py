#Пример фабрика паттерн
import abc
class AbstractTransport(abc.ABC): #на основе этого класса мы создадим реальный транспорт
    def __init__(self,payload):
        self.payload = payload

    @abc.abstractmethod
    def deliver(self):
        raise NotImplementedError('Нельзя использовать абстрактный класс')

class Truck(AbstractTransport):
    def __init__(self,payload,name):
        super().__init__(payload)
        self.name = name

    def deliver(self):
        print(f'Грузовик "{self.name}" выполняет необходимые действия - едет по дороге')


class Ship(AbstractTransport):
    def __init__(self, payload, name):
        super().__init__(payload)
        self.name = name

    def deliver(self):
        print(f'Корабль "{self.name}" выполняет необходимые действия - следует по морю')

#Реализуем фабричный метод - создаём класс Logistics
class Logistics:
    transport = [] #тут будет хранится транспорт
    def __init__(self,list_of_deliveries):
        self.l = list_of_deliveries

    def plan_delivery(self,delivery):
        #delivery - Одна заявка на доставку = ['груз','тип транспорта']
        if delivery[1] == 'море':
            self.transport.append(Ship(delivery[0],f"Корабль №{len(Logistics.transport)}"))
        elif delivery[1] == 'суша':
            self.transport.append(Truck(delivery[0],f"Грузовик №{len(Logistics.transport)}"))

tasks = [
    [500,'суша'],
    [150_000,'море'],
    [100,'суша'],
    [2000,'суша'],
    [10_000,'море'],
]
boxberry = Logistics(tasks) #фабрика распределения заявок на транспорт
for t in boxberry.l:
    boxberry.plan_delivery(t)
for index,t in enumerate(boxberry.transport):
    print('Заявка №',index+1,end='\t')
    t.deliver()




