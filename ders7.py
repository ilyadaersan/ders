"""try:
    number = int(input("enter a number"))
except:
    print("bir hata oluştu")
"""

"""
 try:
    age = int(input("yaşınızı giriniz"))
    print(age + "yaşındasınız")
except ValueError:
    print("Yanlış yaş değeri girdiniz")
except TypeError:
    print("bir hata oluştu")
 """
"""
while True:
    try:
        age = int(input("yaşınızı giriniz"))
    except ValueError:
        print("yanlış değer girdiniz")
    else:
        print(age,  "yaşındasınız")
        break
    finally:
        print("döngü çalıştı")
"""
"""
try:
    number = int(input("enter a number"))
    if number > 0:
        result = number / 0
    elif number < 0:
        raise ValueError("number must be greater than zero")

except ValueError as exceptionObject:
    print(exceptionObject)
except ZeroDivisionError as xde:
    print(f'error: {xde}')
finally:
    print("this line always will be executed")
"""

def sum(numbers):
    result = 0
    for number in numbers:
     result += number
    return result
def cikarma(numbers) :
    result = 0
    for number in numbers:
     result -= number
     return result
def bölme(numbers):
    result = 0
    for number in numbers:
     result /= number
    return result
def carpma(numbers):
    result = 0
    for number in numbers:
      result *= number
    return result

def getnumbers():

    numbers = list()

    while True:
        number = input(" bir sayı giriniz:")
        if number == "":
            break

        numbers.append(number)
    print(numbers)
    return numbers



def selectOperation(numbers):
    operation = input("Please select an operation: \n" +
                      " + for addition\n" +
                      " - for substraction\n" +
                      " * for multiplication\n" +
                      " / for division\n"
                      )

    if operation == "+":
        print(sum(numbers))
    if operation == "-":
        print(cikarma(numbers))
    if operation == "/":
        print(bölme(numbers))
    if operation == "*":
        print(carpma(numbers))

while True:
    selectOperation(getnumbers())

    select = input("to continue select Y-N")
    if select == "Y":
        continue
    else:
        print("bye bye")
        break




