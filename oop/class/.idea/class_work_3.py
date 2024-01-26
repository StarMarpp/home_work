class Vehicle:
    def __init__(self, wheels):
        self.body = 'metal'
        self.wheels = wheels

    def move(self):
        print('i can move')

class Car(Vehicle):
    def bip_bip(self):
        print('i can bip bip')

class Tractor(Vehicle):
    def __init__(self, wheels, amunition):
        super().__init__(wheels)
        self.color = "Blue"
        self.amunition = amunition

    def plow(self):
        print('i can plow')

new_car = Car(4)
print(new_car.body)
new_car.move()
new_car.bip_bip()