"""

EP5

"""


print("""

Faktöriyel bulma programı.

Çıkmak için 'q' ya basın.

""")

while True:

    sayi = input("Sayı: ")

    if sayi.isalpha():
        print("Program sonlandırılıyor.")
        break


    else:

        sayi = int(sayi)
        factorial = 1

        for i in range(2, sayi+1):

            print("Faktöriyel", factorial, "i:", i)
            factorial *= i
        print("Faktöriyel", factorial)





