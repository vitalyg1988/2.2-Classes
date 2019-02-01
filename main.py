from pprint import pprint

print('Добро пожаловать на ферму дядюшки Джо!')

class Animals():
    satiety = True

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def voice(self, song):
        print(song)

    def state_of_satiety(self):
        if self.satiety:
            print('Не нужно кормить')
        else:
            print('Нужно покормить')


class Horned(Animals):
    Horns = True

class Cows(Horned):
    milk = True

    def get_milk(self):
        if self.milk:
            self.milk = False
            print('Пора доить!')
            return self.milk
        else:
            print('Уже подоили!')

    def voice(self, song='Мычит как Корова'):
        self.voice(song)

class Goats(Cows):

    def voice(self, song='Блеет как Козы'):
        super(Goats, self).voice(song)

class Sheep(Horned):
    haircut = True

    def voice(self, song="Блеет как овцы"):
        super(Sheep, self).voice(song)

    def do_haircut(self):
        if self.haircut:
            self.haircut = False
            print('Пора стричь')
            return self.haircut
        else:
            print('Не нуждается в стрижке шерсти')


class Birds(Animals):
    wings = True

class Waterfowls(Birds):
    swiming = True

class Hens(Birds):
    flying = False
    eggs = True

    def get_eggs(self):
        if self.eggs:
            self.eggs = False
            print('Пора собирать яйца')
            return self.eggs
        else:
            print('Яйца уже собраны')

    def voice(self, song='Кукарекает как курица'):
        super(Hens, self).voice(song)

class Ducks(Hens, Waterfowls):
    flying = True

    def voice(self, song='Крякает как утка'):
        super(Ducks, self).voice(song)

class Geese(Ducks):

    def voice(self, song='Лает как Гусь'):
        super(Geese, self).voice(song)



cow = Cows('Манька', 400)
goat1 = Goats('Рога', 55)
goat2 = Goats('Копыта', 65)
sheep1 = Sheep('Барашек', 97)
sheep2 = Sheep('Кудрявый', 104)
geese1 = Geese('Серый', 10)
geese2 = Geese('Белый', 11)
duck = Ducks('Кряква', 3)
hen1 = Hens('Ко-ко', 2)
hen2 = Hens('Кукареку', 1.5)


