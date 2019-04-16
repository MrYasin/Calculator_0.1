"""

Problem 1

Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez

"""

#### ADDED FUNCTION BECAUSE WHY NOT? ####



def problem1(boy, kilo):

    body_index = kilo / (boy ** 2)

    if body_index < 18.5:
        print(body_index, "\nZayıf.")

    elif body_index >= 18.5 and body_index < 25:
        print(body_index, "\nNormal.")

    elif body_index >= 25 and body_index < 30:
        print(body_index, "\nFazla Kilolu.")

    else:
        print(body_index, "\nObez.")

"""

#ZAYIF
problem1(1.82, 50)

#NORMAL
problem1(1.76, 74)

#FAZLA KİLOLU
problem1(2.12, 123)

#OBEZ
problem1(2.12, 423)


"""






"""


Problem 2

Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.


"""


#### INSTEAD OF ITERATION MADE IT WITH ---MAX--- BECAUSE I'M LAZY ####


a = int(input("Birinci Sayı: "))

b = int(input("İkinci Sayı: "))

c = int(input("Üçüncü Sayı: "))


print("En büyük sayı: ", max(a,b,c))




"""


Problem 3

Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF



"""


vize1 = int(input("1. Vize notu: "))
vize2 = int(input("2. Vize notu: "))
final = int(input("Final notu: "))

calculation = vize1 * 3/10 + vize2 * 3/10 + final * 4/10

if calculation >= 90:
    print("AA")

elif calculation >= 85:
    print("BA")

elif calculation >= 80:
    print("BB")

elif calculation >= 75:
    print("CB")

elif calculation >= 70:
    print("CC")

elif calculation >= 65:
    print("DC")

elif calculation >= 60:
    print("DD")

elif calculation >= 55:
    print("FD")

else:
    print("FF")






"""


Problem 4

Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;


"""


question = input("Üçgen mi Dörtgen mi? (3 -- 4): ")

if question == "4":

    a = int(input("a kenarın uzunluğu: "))
    b = int(input("b kenarın uzunluğu: "))
    c = int(input("c kenarın uzunluğu: "))
    d = int(input("d kenarın uzunluğu: "))


    if a == b and a == c and a == d:
        print("K A R E")
        alan = a * 4
        print("Alan:", alan)

    elif a == c and b == d:
        print("D İ K D Ö R T G E N")
        alan = a * b
        print("Alan:", alan)

    else:
        print("Y A M U K")
        h = int(input("h Yüksekliğini gir: "))
        alan = (a + b / 2) * h
        print("Alan:", alan)



if question == "3":

    a = int(input("a kenarın uzunluğu: "))
    b = int(input("b kenarın uzunluğu: "))
    c = int(input("c kenarın uzunluğu: "))

    if ( abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):

        if a == b and a == c:
            print("Eşkenar Üçgen.")

        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar Üçgen")

        else:
            print("Çeşitkenar Üçgen")

    else:
        print("Üçgen belirtmiyor")
