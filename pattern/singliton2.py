class Singliton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None: #если ранее объекта не было
            Singliton()
        return Singliton.__instance

    def __init__(self):
        if Singliton.__instance != None:
            raise Exception('Объект уже создан!')
        else:
            Singliton.__instance = self

s = Singliton()
print(id(s))
s2 = Singleton.getInstance()
print(id(s2))

