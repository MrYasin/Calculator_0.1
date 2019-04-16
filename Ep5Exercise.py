"""


Problem 1

Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)


"""

print("""
********************
  PERFECT NUMBER 
********************
""")

sayi = int(input("Sayı:\n"))

i = 1
toplam = 0

while i < sayi:

    if sayi % i == 0:
        toplam += i

    i += 1

if toplam == sayi:
    print("{} mükemmel sayı.".format(sayi))
else:
    print("{} mükemmel sayı değil.".format(sayi))





"""


Problem 2¶

Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4


"""

print("""
********************
  ARMSTRONG NUMBER
********************
""")

num = input("Enter a number:\n")
order = len(num)
num = int(num)
sum = 0
temp = num

while temp > 0:

    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is NOT an Armstrong number")



"""


Problem 3

1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.

İpucu: İç içe 2 tane for döngüsü kullanın. Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin.


"""

print("""
********************
MULTIPLICATION TABLE
********************
""")

for num in range(1,11):
    print("**************")
    for x in range(1,11):
        print("{} x {} = {}".format(num,x, num*x))


"""


Problem 4

Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.

İpucu : while döngüsünü sonsuz koşulla başlatın ve kullanıcı q'ya basarsa döngüyü break ile sonlandırın.


"""


print("""
********************
   SUM OF NUMBERS
********************
""")


sum = 0

while True:
    num = input("Number: ")

    if num.isalpha():
        print("\nShutting Down\n")
        break

    num = int(num)
    sum += num

print("Sum of all input's is {}".format(sum))


"""


Problem 5

1'den 100'e kadar olan sayılardan sadece 3'e bölünen sayıları ekrana bastırın. Bu işlemi continue ile yapmaya çalışın.


"""


print("""
********************
 RANGE(101) %3 = 0
********************
""")

for num in range(101):

    if num % 3 != 0:
        continue
    print(num)



"""


Problem 6

Buradaki problemin çözümünü derslerimizde özellikle öğrenmedik. Burada mantık yürüterek ve list comprehension kullanarak 1'den 100'e kadar olan sayılardan sadece çift sayıları bir listeye atmayı yapmayı çalışın.

Not: Programlamada her detayı öğrenemeyiz. Bunun için bazı yerlerde deneme yanılma yoluyla da öğrendiğimiz şeyler olur. Bu problemde deneme yanılma yoluyla list comprehension'ın koşullu durumlarla kullanımını öğreneceksiniz.

İpucu: Basit düşünmeye çalışın.


"""


print("""
********************
  %2 in RANGE(101)
********************
""")


mod_2 = [num for num in range(101) if num % 2 == 0]

print(mod_2)





