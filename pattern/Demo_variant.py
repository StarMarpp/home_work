class AirCastle:
    def __init__(self, height, count_clouds, color, transparency):
        self.color = color
        self.count_clouds = count_clouds
        self.height = height
        self.transparency = transparency

    def change_height(self, value):
        if value <= 0:
            raise ValueError('Высота не может быть отрицательной или ноль')
        else:
            self.height += value

    def plus_num(self, n):
        self.count_clouds += n
        self.height += n // 5

    def visibility(self):
         return int(self.height // self.transparency * self.count_clouds)

    def __str__(self):
        return f"The AirCastle at an altitude of {self.height} meters is {self.color} with {self.count_clouds} clouds”

    def equal(self, other):
        return (self.height, self.color, self.count_clouds) == (other.count_clouds, other.height, other.color)

    def max(self, other):
        return (self.height, self.color, self.count_clouds) > (other.count_clouds, other.height, other.color)

    def min(self, other):
        return (self.height, self.color, self.count_clouds) < (other.count_clouds, other.height, other.color)

    def not_equal(self, other):
        return (self.height, self.color, self.count_clouds) != (other.count_clouds, other.height, other.color)
    raise NotImplementedError