# Задача №3.
# Определите суперкласс Student, включающий:
#
# конструктор, инициализирующий имя студента, его группу(по умолчанию None) и стипендию (по умолчанию 0);
# метод экземпляра для повышения стипендии на какую-то часть (например, на 0.3, т.е. на 30%) с округлением результата до копеек;
# магический метод __str__ для перегрузки строкового представления объекта, который должен выводить данные о студенте в
# формате 'Атрибут: объект.атрибут' по одной записи на каждой строке.
#
# Также определите подкласс Староста, наследующий суперкласс Студент и переопре­деляющий метод повышения стипендии таким
# образом, чтобы он еще больше повышал стипендию за счет дополнительного бонуса в виде какой-то части стипендии.
# Далее:
# создайте экземпляр иван_студент созданного подкласса с начальной стипендией в 2000 рублей;
# повысьте студенту стипендию за отличную учебу на  0.335 и бонуса за научную деятельность в 0.25;
# выведите строковое представление объекта экземпляра с информацией о студенте на экран.
#
# Проделайте те же процедуры со старостой
# Расширение задачи про студента агрегацией:
# Создаём класс группа, в котором будет храниться список студентов, и нам нужн ореализовать подсчет общей стипендии группы.


class Student:
    def __init__(self,name, group=None, schoolarship=0):
        self.name = name
        self.group=group
        self.schoolarship=schoolarship

    def increase(self,percent:float):
        self.schoolarship = round(self.schoolarship*(1+percent),2)

    def __str__(self):
        return f"name: {self.name}\ngroup:{self.group}\nschoolarship:{self.schoolarship}"

class starosta(Student):
    def increase(self,percent:float,extra=0.1):
        self.schoolarship = round(self.schoolarship*(1+percent+extra),2)

class group:
    def __init__(self,*args:Student):
        self.student_list=[]
        for student in args:
            self.student_list.append(student)
    def total_schoolarship(self):
        total_sum =sum([student.schoolarship for student in self.student_list])
        return(total_sum)
student_list = []
for i in range(10,20):
    student_list.append(Student(f'Студент №{i}','k111',i*100))

k111 = group(*student_list)

print(k111.total_schoolarship())
