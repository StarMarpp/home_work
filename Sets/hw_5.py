s = int(input('Группы учеников '))
student = int(input('Количество учеников '))
lang = int(input('Количество языков '))
both = set() #all students
cort = set() #know lang
for i in range(student):#цикл для каждого школьника
    m = int(input('Введите количество языков, который знает школьник '))
    languages = set()
    for i in range(m):
        lang1 = input('Введите язык, который знает школьник ')
        languages.add(lang1)
        cort.add(lang1)

        both |= languages #Добавление языков текущего школьника в общее множество языков
        cort |= languages #Обновление множества языков, которые знает хотя бы один школьник

    print(len(both), "-", list(both))     # Вывод языков, которые знают все школьники

    print(len(cort), "-", list(cort))     # Вывод языков, которые знает хотя бы один школьник

