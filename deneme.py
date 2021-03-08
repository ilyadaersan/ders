k = "ilyadaersan"
s = "abbcd"

kullanıcı = input("kullanıcı adınızı girin")
sifre = input("sifreyi girin")

if kullanıcı == k and sifre != s:
    print("kullanıcı adı doğru fakat sifre yanlış")
elif sifre == s and kullanıcı != k:
    print("sifre doğru fakat kullanıcı adı hatalı")
elif sifre != s and kullanıcı != k:
    print("ikisi de yanlış")
else:
    print("doğru")
