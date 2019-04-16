"""


EP 5


"""


print("""

SOKBANK ATM

Yapabileceğiniz işlemler;

1. Bakiye sorgulama

2. Para Yatırma

3. Para Çekme


Çıkış yapmak için 'Q' ya basın.

""")


bakiye = 1000

while True:

    islem = input("Yapmak istediğiniz işlemi seçin:\n")

    if islem == "q":
        print("\nÇıkış Yapılıyor.")
        break

    elif islem == "1":
        print("Bakiyeniz {} TL.".format(bakiye))

    elif islem == "2":
        miktar = int(input("Miktarı giriniz:\n"))
        bakiye += miktar

    elif islem == "3":
        miktar = int(input("Çekmek istediğiniz miktarı girin:\n"))

        if bakiye - miktar < 0:
            print("Yetersiz bakiye.\n")
            continue

        bakiye -= miktar
        print("İşlem başarılı.\n")

    else:
        print("Geçersiz işlem.\n")
        continue





