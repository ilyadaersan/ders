"""import random
chars = "abcdefglmnoprsxz!-+%123456789"
password = random.choice(chars)
password = ""

for i in range(random.randint(8, 16)):
    password += str(random.choice(chars))
print(password)"""

"""def artikyil(yil):
    if yil % 4 == 0:
       if yil % 100 == 0:
          if yil % 400 == 0:
            return True
       else:
           return True
    else:
         return False


for year in range(2020, 1900, -1):
    if artikyil(year):
        print(year, "bir artık yıldır")"""

"""list = list()
list1 = [1, 2, 3, 4, 5]
print(list1[4])

for index in list1:
    print(type(index))"""

list = [54, 44, 21, 64, 12]
max = 0

for i in list:

    if i > max:
        max = i
    if i < max:
        min = i
print(max)
print(min)

def min(list):
    min = list[0]
    for item in list:
        if item < min:
            min = item
    return min


def max(list):
    max = 0
    for item in list:
        if item > max:
            max = item
    return max

print(max(list))
print(min(list))


























