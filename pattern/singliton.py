class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psd = psw
        self.port = port

    def connect(self):
        print(f'соединение с БД: {self.user}, {self.psd}, {self.port}')

    def close(self):
        print('закрытие соединения с БД')

db = DataBase('root', '1234', 80)
db2 = DataBase('roo33t', '18834', 890)
print(id(db), id(db2)) #проверили, что в классе возможен только один экземпляр класса
# db.connect()
# db2.connect()


# синглетоны применяются для организации доступа к ограниченному ресурсу




