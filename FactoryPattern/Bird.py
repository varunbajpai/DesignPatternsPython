from FactoryPattern.AbstractAnimalClass import AbstractAnimalClass


class Bird(AbstractAnimalClass):

    def __init__(self):
        super().__init__()

    def speak(self):
        return "quack"

    def fly(self):
        return "A bird can easily fly"