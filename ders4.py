"""
index = 1
while index <= 5:
    print(index)
    index = index + 1
import random

randomNumber = random.randint(1, 5)
index = 0
while index < 3:
    guess = int(input("enter your guess"))
    index += 1
    if guess == randomNumber:
        print("you won")
        break
    else:
       print("sorry,you lost")


for index in range(1, 6):
    print(index)
print("done")

numbers = [13, 15, 12, 75, 36, 98, 48, 23, 96]
print(numbers)
for number in numbers:
    print(number)

nums = [12, 37, 48, 63, 87, 32, 90]
for i in nums:
    if i % 2 == 0:
        print(i, " is even number")
    else:
        print(i, " is odd number") """

for outterIndex in range(1, 6):
    for InnerIndex in range(1, 6):
        """print("outterIndex", outterIndex)
        print(InnerIndex)
        print(f"{outterIndex*InnerIndex:4}", end="")
        if InnerIndex == 2:
            continue

firstname= "ilayda"
lastname= "ersan"
print(firstname + "" + lastname + " welcome!")
print(f'    {firstname} {lastname}')"""

#def greetUser():
    #firstName = "ilayda"
    #lastName = "ersan"
    #print(firstName + " " + lastName + " " + "welcome")
    """ ya da  
    def greetUser(firstname, lastname):
    print...
    greetuser("ilaydaa", "ersan")"""
#greetUser()



 """def calculateSum(num1:int, num2:int) -> int:
    sum = num1 + num2 
    return sum

sum = calculateSum(5,6)
print(sum)"""

"""def validateEmail(email):
    if email.count("@") != 1:
        return False
    numberOfdots = email.count(".", email.find('@'))
    if numberOfdots != 1:
        return True
    return True

email = input("enter your email")
if validateEmail(email):
    print("valid email")
else: 
    print("invalid email")

def greet(name):
    message = "a"
    """

import random
chars = "abcdefglmnoprsxz!-+%123456789"
password = random.choice(chars)
password = ""

for i in range(8):
    password += str(random.coice(chars))
print(password)


