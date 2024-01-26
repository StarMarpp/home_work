# Проанализируйте код-пример. Разработайте на его основе программу – логер, которая
# записывает в файл выполненные программой команды сложения и
# вычитания и результаты этих операций.

# with open('new.txt','a',encoding='utf-8') as f: #первый вариант
#     f.write('Вторая-запись\n')
# f = open('new.txt','a',encoding='utf-8')
# f.write('новая строка\n') f.close()

#синглтон на прктике - логер
import datetime
from time import sleep
class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None: #если ранее объекта не было
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Объект-одиночка уже создан!")
        else:
            Singleton.__instance = self

filename = datetime.date.today()
class MyLoger(Singleton):
    def __init__(self):
        super().__init__()
        self.file = open(str(datetime.date.today())+'.txt','a')
        self.file.write('Файл открыт, время:'+str(datetime.datetime.now())+'\n')
    def log_it(self,s):
        t = f"[{str(datetime.date.today())} | {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}] "
        self.file.write(t+s+'\n')

log = MyLoger()
sleep(2)
log.log_it('пробная строка №1')
sleep(2)
log.log_it('пробная строка №2')





