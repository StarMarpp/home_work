# Создайте 2 класса: Pin (штырь) с атрибутами a и b - размеры сторон и Hole(отверстие)
# с атрибутом r - радиус. Штырь имеет прямоугольнуюформу. Отверстие - круглую
# Определите внутри класса Pin метод - outer_circle, возвращающий радиус описанной окружности.
# Определите внутри класса Circle метод is_fit,
# и принимающий на вход экземпляр класса Pin и проверяющий - вошёл ли штырь в отверстие.
# Результатом проверки может быть True/False или текстовое сообщение с результатом.
# Создайте 1 отверстие и несколько штырей разного размера. Проверьте работоспособность


class Pin:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def outer_circle(self):
        r = ((self.a / 2) ** 2 + (self.b / 2) ** 2) ** 0.5
        return r


class Circle:
    def __init__(self, r):
        self.r = r

    def is_fit(self, pin):
        try:
            result = pin.outer_circle() <= self.r
            return result
        except:
            return 'Неверное значение'


p1 = Pin(6, 8)
c1 = Circle(3)
c2 = Circle(5)
print(c2.is_fit(p1))
