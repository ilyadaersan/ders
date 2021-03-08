number = int(input("enter number"))
if number == 0:
    print("number equal to 0")
if number < 0:
    print("number is negative")
if number > 0:
    print("number is positive")


if bool(number):
    print("number is equal to zero")

# if number > 5 and number < 8:
    print("number between 5 and 8")

if 8 > number > 5:
    print("number between 5 and 8")

if number > 5 or number < 10:
    print(number)


list1 = []
list2 = []
list3 = []

if list1 == list2:
    print("true")
else:
    print("false")

if list1 is list2:
    print("true")
else:
    print("false")

firstName = "ilayda"
for letter in firstName:
    print(letter)

if "i" in firstName:
    print(firstName + " contains i ")
else:
    print(firstName + " not contains i ")

number = 0
alphabet = "abcdef"

for char in alphabet:
    print(char)
    number += 1
    print(number)

for number in range(1, 10, 2):
    print(number, end=" ")

number = 0
while True:
    number += 1
    if number % 10 == 0:
        print(number)
    if number == 30:
        break

while number < 30:
    number += 1
    if number % 10 == 0:
        print(number)




