import random

randomNumber = random.randint(1, 50)
index = 5
while True:
    guess = int(input("enter your guess"))
    index -= 1
    if guess < randomNumber:
        print("sayıyı yükseltiniz")
    elif guess > randomNumber:
        print("sayıyı azaltınız")
    else:
        print(("doğru bildiniz."))
        break
    if index == 0:
        print("Tahmin Bitti Üzgünüm Kaybettiniz")
        break
print(randomNumber)


