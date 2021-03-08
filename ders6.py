"""number = [1, 2, 3, 4, 5]
letters = ["a", "b", "c", "d"]
sum = letters + number
number = number[0] * 2
print(sum)
print(number)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = []
for number in numbers:
    squares.append(number ** 2)

print(squares)"""
"""the same solution"""

"""squares2 = [number ** 2 for number in numbers]
print(squares2)
numbers = [number for number in range(2, 1001, 2) if number % 3 == 0]
print(numbers)
"""or"""
number2 = []
for number in range(2, 1001, 2):
    if number % 3 == 0:
        numbers.append(number2)
print(numbers)

names = ["Orçun", "jale", "berk", "osman", "Onur"]
names1 = [name for name in names if name[0] == "o" or name[0] == "O"]
print(names1)

"""
"""list = [20,30,40]
list2 = [2,3,4,5]
newlist = []
unique = []
for x in list:
    for y in list2:
        newlist.append(x*y)
        if x*y not in unique:
            unique.append(x*y)

print(newlist)
print(unique)
newlist1 = [x*y for x in list for y in list2 if x*y <= 100]
print(newlist1) """
"""
names = []
index = 0

while True:
    name = input("enter name")

    if name == "" and index > 5:
        break

    if name in names:
        print(name)
    else:
        names.append(name)
        index += 1
print(names)

"""
"""
string = "This is a python exercise python python python"
unique = []
string = string.split(" ")



for word in string:
    if word not in unique:
        unique.append(word)
print(len(unique), " tane kelime bulunuyor")


print(unique)


tuple = (1,2,3,4,5,6,7,8,9,10)
print(tuple)
print(type(tuple))
tuple2 = (1)
print(tuple2)
print(type(tuple2))


import sys
import timeit
evenNumbers = [number for number in range(2,1001,2)]
evenTuple = tuple(evenNumbers)
print("list size", sys.getsizeof(evenNumbers))
print("tuple size", sys.getsizeof(evenTuple))

print("list time test", timeit.timeit(stmt="number = [1,2,3,4,5]"))
print("tuple time test", timeit.timeit(stmt="number = (1,2,3,4,5)"))

tuple = (1,2,3,4,5,6,7,8,9,10,5)
print(tuple[0])
print(tuple[8])
print(tuple[-2])
print(tuple[2:])
print(tuple.count(5))
print(3 in tuple)
del tuple
print(tuple)"""""""""
"""
bannedwords = ["aq", "amk"]

while True:
    string = ""
    userInput = input("bir cümle gir:")
    words = userInput.split(" ")
    if userInput == "":
        break

    for word in words:
        if word in bannedwords:
            string += "..."
        else:
            string += " " + word

    print(string)
    """
"""dict1 = {}
print(type(dict1))

customers = {
    "name": "Berk Açıkel",
    "email": "berkacikel@gmail.com",
    "phonenumber": "5430403897",

}
print(customers)
customers1 = dict(name = "berk açıkel", email = "berkacikel@gmail.com", phonenumber = "5430403897")
print(customers1)
print(customers1["name"])
customers1["tc"] = "83487549857"
print(customers1)

dictlist = {"numbers":
                {"number":1, "number2":2, "number3":3},

            "cities":{
                "city1": "izmir", "city2":"istanbul", "city3":"ankara"
            },
            }
print(dictlist["cities"]["city1"])
print(dictlist.get("cities", 0).get("city1",))
"""

#squares = {1: 1, 2: 4, 3: 9, 4: 16}
#print(squares)
#print(squares.pop(4))
#print(squares.popitem())
#print(squares)
#squares.clear()
#print(squares)

#print(squares.items())

#keys = []
#values = []
#for k,v in squares.items():
   # print(f'Key is {k}')
   # print(f'Value is {v}')

   # for item in squares:
        #print(f'key: {item} value: {squares.get(item)}')

"""person = {'name': 'ali', 'age': 20}
#person.popitem()
#age = person.setdefault("age", 25)
#print(person)

person.update({'name': 'batuhan'})
print(person)

people = {1: {"name": "ali", "age": 20},
          2: {"name": "mehmet", "age": 30},
          3: {"name": "batuhan", "age": 24}, }


for x in people:
    print(people.get(x).get("name"))



for k, v in people.items():
    print(f'key {k} - value {v}')
    print(v.get("name"))

    if v.get("age") > 25:
        add = v.get("age")
        add += 5
        v.update({"age": add})
print(people)
"""
"""list1 = [1, 1, 2, 3, 4, 5]
print(list1)
unq = set(list1)
print(unq)
setlist = {1, 2, 3, 4, 5}
print(type(setlist))

setlist1 = {1.0, 2, "hello", (1, 2, 3), 1}
print(type(setlist1))
print(setlist1)

myset = set()
print(type(myset))
#myset = {}
#print(type(myset))
myset.add(4)
myset.add(3)
myset.add(2)
myset.add(3)
myset.add(3)
print(myset)

myset.update([2,5,8])
myset.update([0,10],(5,7))
print(myset)

myset.discard(2)
print(myset)
myset.pop()
print(myset)
"""

A = {100, 10, 20, 30, 4}
B = {100, 1, 2, 3, 4}
#setlist = A | B
setlist = A.union(B)
print(f'setlist after union {setlist}')

setlist = A & B
setlist = A.intersection(B)
print(f'setlist after union {setlist}')

setlist = A - B
setlist = A.difference(B)
print(f' setlist after dif { setlist}')

setlist = A ^ B
setlist = A.symmetric_difference(B)
print(f'setlist after sys dif {setlist}')
















