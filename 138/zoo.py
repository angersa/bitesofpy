
class Animal:
    idx = 10000
    zoo_lst = list()

    def __init__(self, name):
        self.name = name.title()
        Animal.idx += 1
        Animal.zoo_lst.append(f'{Animal.idx}. {self.name}')

    def add_animal(self):
        animal = (self.idx, self.name)
        zoo_lst.update(animal)

    def __str__(self):
        return f'{self.idx}. {self.name}'

    @classmethod
    def zoo(cls):
        return cls.zoo_lst
