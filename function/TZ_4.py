"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""

def schet_massa(weight, height):
    imt = int(weight / (height * height))

def realise(weight, height):
    schet = schet_massa(weight, height)
    if int(schet) >= 0 and int(schet) <= 18.5:
        print('Недостаточный вес')
    elif int(schet) >= 18.5 and int(schet) <= 25:
        print("ИМТ в норме")
    elif int(schet) > 20:
        print('Избыточный вес')

weight = int(input('Вес: '))
height = int(input('Рост: '))

realise(weight, height)




