from abc import ABCMeta, abstractmethod
"""abstra Meta. We can't use it to set up an object. it is used by the other meta to inheritate"""

class Pet(object, metaclass = ABCMeta):
    """Pets"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):
    """DOg"""
    def make_voice(self):
        print('%s : wangwangwang...' % self._nickname)

class Cat(Pet):
    """Cat"""
    def make_voice(self):
        print('%s :miaomiaomiao ...' %self._nickname)

def main():
    pets = [Dog('wangcai'), Cat('xiaohua'), Dog('boy')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()