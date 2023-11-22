""" Напишите декоратор печатающий время выполнения данной функции. """

from time import time
def time_decor(func):
    def wrapper():
        start = time()
        func()
        end = time()
        total = end - start
        print(total)
    return wrapper

@time_decor
def func_to_decor():
    for i in range(1000):
        print(i)

func_to_decor()

