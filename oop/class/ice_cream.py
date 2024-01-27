class Icecream:
    def __init__(self, topping=None, sprinkles=None):
        self.topping = topping
        self.sprinkles = sprinkles

    def show_my_icecream(self):
        if self.topping and self.sprinkles:
            print(f'Мороженное с {self.topping} топингом и {self.sprinkles} посыпкой')
        elif self.topping and not self.sprinkles:
            print(f'Мороженное с {self.topping} топингом')
        elif self.sprinkles and not self.topping:
            print(f'Мороженное с {self.sprinkles} посыпкой')
        else:
            print('Мороженное без добавок...')


class Topping:
    def __init__(self, flavor):
        self.title = flavor
class Sprinkles:
    def __init__(self,flavor):
        self.title = flavor
sprinkles = ['Орехи','карамель','цветные шарики','шоколадная крошка']
toppings = ['Шоколад','Клбуника','Карамель','Сгущенка','Фисташка']
s_list=[]
t_list=[]
for flavor in sprinkles:
    s_list.append(Sprinkles(flavor))
for flavor in toppings:
    t_list.append(Topping(flavor))
print(*t_list,sep=', ')
print(*s_list,sep=', ')
chocolate_topping_icecream= Icecream(t_list[0])
new = Icecream(t_list[2],s_list[3])
chocolate_topping_icecream.show_my_icecream()
new.show_my_icecream()
