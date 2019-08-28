from FactoryPattern.AbstractAnimalClass import AbstractAnimalClass

class Dog(AbstractAnimalClass):

    def __init__(self):
        super().__init__()

    def speak(self):
        return "Woof"

    def fly(self):
        return "The Dog does not fly"