# Создать класс товар с атрибутами Name,
# Price Создать класс список покупок с методами:
# добавить товар, удалить товар, общая стоимость

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f'Товар: {self.name}, ({self.price} рублей)'
class List_product(Product):

    def __init__(self,insert, delete):
        self.shoplist = []
    def add_to_shopcars(self,product):
        self.shoplist.append(product)
    def remove_from_shopcart(self):
        for id, product in enumerate(self.shoplist):
            print(id+1, ')', product, sep='', end='\n')
        x = int(input('Введите номер товара '))
        self.shoplist.pop((x-1))
        print(f"Товар{self.shoplist.pop(x-1)} удален")

    def total(self):
        result = 0
        for p in self.shoplist:
            result += p.price
            print([p.price for p in self.shoplist])
            print('итоговая цена:', result)

potato = Product('Картофель',40)
cucumber = Product("Огурец", 60)
