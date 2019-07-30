class Person(object):
    #限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age<= 16:
            print('%s is flying.'%self.name)
        else:
            print('%s is running'%self.name)

def main():
    person = Person('wang', 22)
    person.play()
    person._gender = 'male'
    person._money=100  #用了slots后这一行会报错
main()