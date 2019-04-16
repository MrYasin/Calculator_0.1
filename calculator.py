"""


CALCULATOR EXERCISE ON UDEMY


"""



print("""

Hesap Makinesi Programı

İşlemler;

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşlemi


""")


a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))

islem = int(input("İşlemi giriniz: "))

if islem == 1:

    print("{} ile {} in toplamı {}'dir".format(a, b, a + b))

elif islem == 2:

    print("{} ile {} in farkı {}'dir".format(a, b, a - b))

elif islem == 3:

    print("{} ile {} in çarpımı {}'dir".format(a, b, a * b))

elif islem == 4:

    print("{} ile {} in bölümü {}'dir".format(a, b, a / b))

else:
    print("Geçerli işlem indexi girin.")





