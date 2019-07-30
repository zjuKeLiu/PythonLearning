class Person(object):
    """人"""
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
    def age(Self, age):
        self._age = age

    def play(Self):
        print('%s is enjoying playing.' % self._name)

    def watch(self):
        if self._age >= 10:
            print('%s is playing computer games.' %self._name)
        else:
            print('%s is studying hard.' % self._name)

class Student(Person):
    """students"""
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self, grade):
        self._grade = grade
    def study(self, course):
        print('%s of %s is studying %s.' % (self._name, self._grade, course))

class Teacher(Person):
    """Teacher"""
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title
    @property
    def title(self, title):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title
    def teach(self, course):
        print('%s %s is teaching %s.' %(self._name, self._title, course))

def main():
    stu = Student('wang', 15, 'junior')
    stu.study('math')
    stu.watch()
    t = Teacher('Liu', 38, 'Professor')
    t.teach('Python')
    """bugs"""
    #print(t.name())
    #t.play()
    #stu.name()

if __name__ == '__main__':
    main()