"""


Problem 1

1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).



"""


def perf_num(num):

    sum = 0

    for i in range(1, num):

        if num % i == 0:

            sum += i

    return sum == num


for i in range(1, 1001):
    if perf_num(i):
        print("Perfect numbers are:\n", i)



"""


Problem 2

Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;

http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok


"""


def ebob(num1, num2):

    i = 1
    ebob = 1

    while i <= num1 and i <= num2:

        if not num1 % i and not num2 % i:
            ebob = i

        i += 1

    return ebob

num_1 = int(input("EBOB -- Number 1:\n"))
num_2 = int(input("EBOB -- Number 2:\n"))

print("EBOB: ", ebob(num_1, num_2))



"""


Problem 3

Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.

Problem için şu siteye bakabilirsiniz;

http://www.matematikciler.com/6-sinif/matematik-konu-anlatimlari/1020-en-kucuk-ortak-kat-ve-en-buyuk-ortak-bolen-ebob-ekok


"""


def ekok(num1, num2):

    i = 2
    ekok = 1

    while True:
        if num1 % i == 0 and num2 % i == 0:

            ekok *= i

            num1 //= i
            num2 //= i

        elif num1 % i == 0 and num2 % i != 0:

            ekok *= i

            num1 //= i

        elif num1 % i != 0 and num2 % i == 0:

            ekok *= i

            num2 //= i

        else:
            i += 1

        if num1 == 1 and num2 == 1:
            break

    return ekok



num_1 = int(input("EKOK -- Number 1:\n"))
num_2 = int(input("EKOK -- Number 2:\n"))

print("EKOK: ", ekok(num_1, num_2))




"""


Problem 4

Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi


"""


first =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
second = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def num_read(num):

    first_base = num % 10
    second_base = num // 10

    return second[second_base] + " " + first[first_base]

num = int(input("NUM READ: "))

print(num_read(num))



"""


Problem 5

1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)


"""



def pythagoras():

    pythagoras_list = list()

    for i in range(101):
        for x in range(101):

            c = (i**2 + x**2) ** 0.5

            if c == int(c):
                pythagoras_list.append((i,x,int(c)))


    return pythagoras_list

for i in pythagoras():
    print(i)




















