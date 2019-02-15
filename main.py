from functools import reduce


class Animals:
    satiety = True

    def __init__(self, weight=0.0, name='noname'):
        self.name = name
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def voice(self, song):
        print(song)

    def state_of_satiety(self):
        if self.satiety:
            print('Не нужно кормить')
        else:
            print('Нужно покормить')

    def __add__(self, other):
        return Animals(self.weight + other.weight)


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


class Goats(Cows, Horned):

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
    eggs = True

    def get_eggs(self):
        if self.eggs:
            self.eggs = False
            print('Пора собирать яйца')
            return self.eggs
        else:
            print('Яйца уже собраны')


class Waterfowls(Birds):
    swiming = True


class Hens(Birds):
    flying = False
    eggs = True

    def voice(self, song='Кукарекает как курица'):
        super(Hens, self).voice(song)


class Ducks(Waterfowls, Birds):
    flying = True

    def voice(self, song='Крякает как утка'):
        super(Ducks, self).voice(song)


class Geese(Waterfowls, Birds):
    def voice(self, song='Лает как Гусь'):
        super(Geese, self).voice(song)


cow = Cows(400, 'Манька')
goat1 = Goats(55, 'Рога')
goat2 = Goats(65, 'Копыта')
sheep1 = Sheep(97, 'Барашек')
sheep2 = Sheep(104, 'Кудрявый')
geese1 = Geese(10, 'Серый')
geese2 = Geese(11, 'Белый')
duck = Ducks(3, 'Кряква')
hen1 = Hens(2, 'Ко-ко')
hen2 = Hens(1.5, 'Кукареку')

if __name__ == '__main__':
    animal_list = [cow, goat1, goat2, sheep1, sheep2, geese1, geese2, duck, hen1, hen2]
    max_weight = reduce(lambda weight1, weight2: weight1 if (weight1 > weight2) else weight2, animal_list)
    sum_weight = reduce(lambda weight1, weight2: weight1 + weight2, animal_list)
    print(f'Самое тяжелое животное {max_weight.name}')
    print(f'Общий вес всех животных {sum_weight.weight} кг')
