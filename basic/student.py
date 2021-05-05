#coding: utf-8

class Student():
    name = ""
    age = 0
    gender = ""
    phone = ""
    address = ""
    email = ""
    def __init__(self,name,age,weight,grade,gender,phone,address,email):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.address = address
        self.email = email
    def eat(self):
        print("eat")
    def drink(self):
        print("drink")
    def play(self):
        print("play")
    def sleep(self):
        print("sleep")

student_list = []
Arex = Student("Arex",28,60,19,"male","13166666666","shanghai","arexchu@163.com")
Bob = Student("Bob",18,50,9,"male","13588888888","beijing","zjfbob@163.com")
student_list.append(Arex)
student_list.append(Bob)

while(1):
    name = input("please input the student's name:")
    email = input("please input the student's email:")
    address = input ("please input the student's address:")
    for student in student_list:
        if student.name == name or student.email == email or student.address == address:
            print(student.__dict__)
        elif student_list.index(student) == len(student_list) - 1:
            print("can't find the data. please input the right information.")
