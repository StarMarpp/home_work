#first = "0 0 0 0 0 0 0" #Вывод должен быть 0
#second = "1 1 1 0 0 0 0" # Вывод должен быть 3
#third = "1 1 1 1 1 1 1" # Вывод должен быть 1


A = int(input(('Количество решенных задач на циклы ')))
B = int(input(('Количесвто решенных задач на массивы ')))
C = int(input(('Количество решенных задач на строки ')))
D = int(input(('Количество решенных задач и на циклы, и на массивы')))
E = int(input(('Количество решенных задач на строки, и на циклы')))
F = int(input(('Количество решенных задач на строки, и на массивы')))
G = int(input(('Количество решенных задач и на циклы, и на строки, и на массивы ')))

bigset = A + B + C - (D + E + F - G)
print('Общее количество правильных решенных задач',bigset)



