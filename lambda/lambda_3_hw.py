"""
Напишите список функций по требованию. Пользователь вводит имя.
Если имя заканчивается на А,Я,Г,М, то программа добавляет к имени "Гений".
Если на О,Ь,Л,Н. То добавляется "Сверхразум". Если ни на одну из этих букв то добавляется "Просто" перед именем.
"""
user_name = input('Введите ваше имя: ')
lamda_list = [lambda name: name + ' гений', lambda name: name + ' сверхразум', lambda name: 'просто '+ name ]
while user_name:
    if user_name[-1] in ('а', 'я', 'г', 'м'):
        print(lamda_list [0] (user_name))
    elif user_name [-1] in ('о', 'ь', 'л', 'н'):
        print(lamda_list [1]  (user_name))
    else:
        print(lamda_list [2] (user_name))
    user_name = input('Введите ваше имя: ')