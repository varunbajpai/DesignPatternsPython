from FactoryPattern.Dog import Dog
from FactoryPattern.Bird import Bird


FACTORY_DICT = {
    'dog' : Dog(),
    'bird' : Bird(),
}



def factory(object_type):
    return FACTORY_DICT[object_type]


if __name__ == "__main__":
    dog = factory('dog')
    print(dog.speak())
    bird = factory('bird')
    print(bird.speak())