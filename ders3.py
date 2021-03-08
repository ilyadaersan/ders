"""

userInput = input("kelimeyi azınız")

if userInput[::-1] == userInput:
    print("true")
else:
    print("false")
"""


userIn = "Anne, I vote more cars race Rome-to-vienna"
removedChars = ""
for letter in userIn:
    if letter.isalnum():
        removedChars = removedChars + letter
print(removedChars)




