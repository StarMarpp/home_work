class Hero:
    def __init__(self,name,health,armor,power,weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):
        print('Приветствуем героя:', self.name) #Имя конкретного экзепляра
        print('Вооруженного оружием:', self.weapon)

    def strike(self,enemy): #герой который бьет, enemy - герой по которому бьют
        print(self.name, 'бьет',enemy.name, 'с силой: ', self.power)
        enemy.armor -= self.power #-5
        if enemy.armor <= 0:
            enemy.health += enemy.armor
            enemy.armor = 0
        print('у героя', enemy.name, 'осталось', enemy.health, 'здоровья и', enemy.armor, 'брони')


    def brawl(self,enemy): #методы который выполняет объект.
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)
            enemy.strike(self)
        if enemy.health < self.health:
            print(self.name, 'win')
        elif self.health > enemy.health:
            print(self.name, 'win')

    def rest(self): #отдых восттанавление здоровья



Knight = Hero('Artur',100,50,20, 'Меч')
Archer = Hero("Legolas",100,15,15,"Лук")
Knight.print_info()
Archer.print_info()
#герой экзепляр класса

Knight.brawl(Archer)
