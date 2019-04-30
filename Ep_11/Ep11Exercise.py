



from functools import reduce


"""

Problem 1¶

Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.

         [(3,4),(10,3),(5,6),(1,9)]

Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu listenin her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.

         [12, 30, 30, 9]

Not : map() fonksiyonunu kullanmaya çalışın.

"""


dikgotgen = [(3,4),(10,3),(5,6),(1,9)]

def area(dikgotgen):
    return dikgotgen[0] * dikgotgen[1]


print("\nProblem 1\n")

print(list(map(area,dikgotgen)))



"""


Problem 2

Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

     [(3,4,5),(6,8,10),(3,10,7)]

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.

     [(3, 4, 5), (6, 8, 10)]

Not: filter() fonksiyonunu kullanmaya çalışın.


"""

tuple_2 = [(3,4,5),(6,8,10),(3,10,7)]

def triangle(t):

    if abs(t[0] + t[1] > t[2]) and abs(t[0] + t[2] > t[1]) and abs(t[1] + t[2] > t[0]):
        return True
    else:
        return False

print("\nProblem 2\n")

print(list(filter(triangle, tuple_2)))


"""


Problem 3

Elinizde şöyle bir liste bulunsun.

    [1,2,3,4,5,6,7,8,9,10]

Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.

Not: İlk önce filter() fonksiyonu ile çift sayıları ayıklayın. Daha sonra reduce() fonksiyonunu kullanın.


"""


filt = list(filter(lambda x: x % 2 == 0, range(11)))

print("\nProblem 3\n")
print(reduce(lambda x,y: x + y, filt))


"""

Problem 4

Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste olsun.

        isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

Bu isimleri ve soyisimleri sırasıyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdırın.

Not: zip() fonksiyonunu kullanmaya çalışın.

"""



isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

x = list(zip(isimler, soyisimler))

print("\nProblem 4\n")

for i,j in x:

    print(i,j)























