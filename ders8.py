"""class footballer:
    #attributes
    name = "messi"
    club = "barcelona"
    #behavior
    def walk(self):
        return "footballer walking"

f1 = footballer()
print(f1.name)
print(f1.club)

f1.club = "a team"
print(f1.club)
print(f1)
print(type(f1))


class square:
    #edge = 5

    def __init__(self, edge):
        self.edge = edge

    def area(self):
        self.print2()
        return self.edge * self.edge
    def print2(self):
        print("AAA")

s1 = square(5)
s2 = square(7)
s3 = square(10)
print(s1.edge)
print(s1.area())
print(s2.edge)
print(s2.area())
print(s3.edge)
print(s3.area())"""

"""class animal:
    def __init__(self,a, b,c,d):
        self.name = a
        self.age = b
        self.birthday = c
        self.species = d

k1 = animal("kanguru", 3, "19/09/97", "familya")
k2 = animal("küpek", 1, "19/09/99", "memeli")
k3 = animal("inek", 1, "18/02/99", "memeli")
print(k1.name)
print(k1.age)
print(k2.name)"""

"""class calculater:
    def __init__(self,num1,num2):

        self.num1 = num1
        self.num2 = num2

    def toplama(self):
        return self.num1 + self.num2

    def cikarma(self):
        return self.num1 - self.num2

    def carpma(self):
        return self.num1 * self.num2

    def bölme(self):
        return self.num1 / self.num2

while True:
    try:
        a = int(input("1.sayı"))
        b = int(input("2.sayı"))
    except ValueError:
        print("wrong")
        continue
        
    selection = input(+ - * / )  
    calcobject ==

       








print(calculater.toplama(a))
print(calculater.cikarma(a))
print(calculater.carpma(a))
print(calculater.bölme(a))"""

"""class BankAccount:
    def __init__(self, name, money, address):
        self.name = name #global
        self.__money = money #privacy
        self.address = address

    def getMoney(self):
        return self.__money

    def setMoney(self,amount):
        self.__money = amount


b1 = BankAccount("messi", 1000,"address")
b2 = BankAccount("neymar", 500, "address")"""

"""print(b1.money)
print(b2.money)
print("----")
b2.money = b1.money + b2.money
b1.money = 0
print(b1.money)
print(b2.money)"""
"""
print(b1.getMoney())
print(b2.getMoney())
b2.setMoney(1500)
print()
"""

"""
class Animal:
    def __init__(self):
        print("Animal object created")

    def toString(self):
        print("Animal")

    def walk(self):
        print("Animal walk")


class Monkey(Animal):
    def __init__(self):
        super().__init__()
        print("Monkey created")

    def toString(self):
        print("Monkey")

    def climb(self):
        print("Monkey is climbing")


class Bird(Animal):
    def __init__(self):
        super().__init__()
        print("Bird created")

    def fly(self):
        print("Bird can fly")


m1 = Monkey()
b1 = Bird()
m1.walk()
m1.climb()
m1.toString()"""
"""
class Website:
    def __init__(self,name , surname):

        self.name = name
        self.surname = surname
        print("website created")

    def login(self):
        print(self.name)
        print(self.surname)




class Websitewithlogin(Website):
    def __init__(self,name,surname,id):
        super(Websitewithlogin, self).__init__(name, surname,)
        Website.__init__(self,name,surname)
        self.id = id
    def loginId(self):
        print(self.name)
        print(self.surname)
        print(self.id)


class websitewithemail(Website):
    def __init__(self,name,surname,email):
        #super(websitewithemail, self).__init__(name, surname)
        Website.__init__(self, name, surname)
        self.email = email
        print("email created")

    def loginemail(self):
        print(self.name)
        print(self.surname)
        print(self.email)
w1 = Website("ilayda","ersan")
w1.login()
w2 = websitewithemail("ialyda","ersan","ilaydaersan00@gmail.com")
w2.loginemail()
w3 = Websitewithlogin("ilayda","ersan",31324)
w3.loginId()
"""

class vehicle:
    def __init__(self, id, model, color, year, price):
        self.id = id
        self.model = model
        self.color = color
        self.year = year
        self.price = price

class kdvvehicle(vehicle):
    def __init__(self, id, model, color, year, price,kdv):
        self.kdv = kdv

    def kdvli(self,kdvli):
        self.kdv = kdvli * 1.18
        self.kdv += kdvli





class Bus(vehicle):

    def __init__(self,id,model,color,year,price,people):

        super(Bus, self).__init__(id,model,color,year,price)
        self.people = people


class kdvbus(vehicle):
    def __init__(self,id , model, color, year, price, kdv):
        super(kdvbus,self).__init__(id, model, color, year, price)
        self.kdv = kdv

    def kdvli(self,kdvli):
        self.kdv = kdvli * 1.40
        self.kdv += kdvli



class Motorbike(vehicle):

    def __init__(self,id,model,color,year,price,cc,suveyahava):
        
        super(Motorbike, self).__init__(id,model,color,year,price)
        self.cc = cc
        self.suveyahava = suveyahava




class Car(vehicle):

    def __init__(self,id,model,color,year,price,sunrof):
        super(Car, self).__init__(id,model,color,year,price)
        self.sunrof = sunrof

    def KDV3(self):
        
    
        return self.price * 1.64
        
        







a1 = vehicle(115645,"mercedes","red",1998,19.000)
b1 = Bus(115676,"mercedes","black",2018,30.000,34)
c1 = Motorbike(117836,"Harley","grey",2015,16.500,50,"su")
d1 = Car(116734,"BMW","purple",1999,15.800,"yes")

b1.KDV()

















