##클래스##

class Student:
    def start(self):
        print('안녕하세요.')
    def printName(self, name):
        print('제 이름은 {0} 입니다'.format(name))

stu = Student()
Student.start(stu)
stu.printName('파이썬')

##모듈##
