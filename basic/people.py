#coding: utf-8

class People():
    name = ""
    age = 0
    __weight = 0
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.__weight = weight
    def speak(self):
        print("I'm %s.I'm %d years old." % (self.name,self.age))
class Student(People):
    grade = 0
    def __init__(self,name,age,weight,grade):
        super().__init__(name,age,weight)
        self.grade = grade
    def speak(self):
        print("I'm %s.I'm %d years old.I‘m in %dth grade this year" % (self.name,self.age,self.grade))

Arex = Student("Arex",28,60,19)
speak = Arex.speak()
