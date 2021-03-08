vize = int(input("vize:"))
final = int(input("final:"))

vize1 = (vize) * (30 / 100)
final1 = (final) * (70 / 100)
sonuc = vize1 + final1
# sonuc = vize * (3/10 ) + final * (7/10)
if 100 >= sonuc and sonuc >= 85:
    print("A")
else:
    print("sınıfta kaldın ")

