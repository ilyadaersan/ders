tc = input("enter your id card number")
if not len(tc) == 11:
    print("not true")

if int(tc[0]) == 0:
    print("not true")

index = 1
evenTotal = 0
oddTotal = 0
numberTotal = 0

for number in tc:
    numberTotal += int(number)
    if index > 9:
        break

    if int(number) % 2 == 0:
        evenTotal += int(number)
    else:
        oddTotal += int(number)

    if oddTotal * 7 - evenTotal % 10 == int(tc[9]):
        print("tc is true")
    index += 1

userInput = input("yaz")
alphabet = "abcdefghjklmnoprsqw"
count = 0


for letter in userInput:
    count = userInput.count(letter)

    if letter not in newString:
        newString = newString + str(count) + letter
print(newString)












