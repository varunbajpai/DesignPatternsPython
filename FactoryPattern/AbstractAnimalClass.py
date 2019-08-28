from abc import ABC, abstractmethod

class AbstractAnimalClass(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def fly(self):
        pass