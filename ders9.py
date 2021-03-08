"""
from abc import ABC,abstractmethod  #abstract base class

class Animal(ABC):


    @abstractmethod #atama yapmaya yarar
    def walk(self):
        pass

    @abstractmethod
    def run(self):
        pass

class Bird(Animal): # abstractı kullanırsak çocuklarında da kullanmak lazım.
    def __init__(self):
        print("bird class created")

    def walk(self):
        print("bird walk")
    def run(self):
        print("bird run")



a = Bird()
a.walk() """

"""
class Animal:

    def toString(self):
        print("animal")

class Monkey(Animal):

    def toString(self):
        print("monkey")

a = Animal()
a.toString()
m1 = Monkey()
m1.toString()
"""

"""
class Employee:

    def raisee(self):
        raise_rate = 0.1
        return 100 + 100*raise_rate

class ComputerEngineer(Employee):

    def raisee(self):
        raise_rate = 0.2
        return 100 + 100*raise_rate

class Manager(Employee):
    def raisee(self):
        raise_rate = 0.3
        return 100 + 100*raise_rate

e = Employee()
print(e.raisee())

b = ComputerEngineer()
print(b.raisee())

c = Manager()
print(c.raisee())
"""
"""
from abc import ABC,abstractmethod
class shape(ABC):


    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass


class square(shape):
     def area(self):
        pi = 3.14
        r = 5
        print("karenin alanı")
        return r * r


     def perimeter(self):
        pi = 3.14
        r = 5
        print("karenin çevresi")
        return 4 * r

class circle(shape):


    def area(self):
        pi = 3.14
        r = 5
        print("çemberin alanı")
        return pi * r * r

    def perimeter(self):
        pi = 3.14
        r = 5
        print("çemberin çevresi")
        return 2 * pi * r

b = square()
print(b.area())
print(b.perimeter())
c = circle()
print(c.area())
print(c.perimeter())

"""
class CreateStudent:

    def __init__(self,name, password, email, address, contactNumber,stID):
        self.name = name
        self.password = password
        self.email = email
        self.address = address
        self.contactnumber = contactNumber
        self.stID = stID
        print(self.name,self.password,self.email,self.address,self.contactnumber,self.stID)

class Register:
    stulist = 0

    def __init__(self):
        self.stulist = {}

    def createStudent(self):

        name = input("isminizi giriniz.")
        password = input("parolanızı giriniz")
        email = input("emailinizi giriniz")
        address = input("ev adresinizi giriniz")
        contactNumber = int(input("telefon numaranızı giriniz"))
        stID = int(input("ID numaranızı giriniz"))


        student = CreateStudent(name, password, email, address, contactNumber, stID)

    def studentRegister(self,student):
        self.stulist[student.getStdID()] = student

    def display(self):
        for item in self.stulist:
            





def menu():
    selection = input("select action")
    return selection
selection = menu()

while selection != 12:
    if selection == "1":

        a = Register()
        a.createStudent()
        menu()

    elif selection == "2":









