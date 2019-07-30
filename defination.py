#定义类
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self , course_name):
        print('%s is studying %s.' %(self.name, course_name))

    def watch_movie(self):
        if self.age<18:
            print('%s is watching bear .' %self.name)
        else:
            print('%s is watching amazing movie' %self.name)

#向类发送信息
def main():
    #创建一个对象
    stu1 = Student('Tom' , 38)
    #向对象发送信息
    stu1.study('Python')
    stu1.watch_movie()
    #创建第二个对象
    stu2 = Student('Jerry' , 11)
    #向对象发送信息
    stu2.study('running')
    stu2.watch_movie()

if __name__ =='__main__':
    main()
