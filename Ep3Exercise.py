"""


Problem 1

Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.


"""


a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

solution_1 = a * b * c

print("{} x {} x {} = {}".format(a, b, c, solution_1))



""""


Problem 2

Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)


"""

height = int(input("Height: "))
weight = int(input("Weight: "))


print("Body index: ", height / (weight ** 2))


"""


Problem 3

Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünün toplam ne kadar 
ödemesini gerektiğini hesaplayın.


"""

milage = int(input("Milage: "))
distance = int(input("Distance: "))

print("Total: ", milage * distance)


"""


Problem 4

Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.


"""


name = str(input("Name: "))
surname = str(input("Surname: "))
number = int(input("Number: "))

print(name, surname, number, sep="\n")




"""


Problem 5

Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.


"""


number_1 = int(input("First Number: "))
number_2 = int(input("Second Number: "))

print("\n Current order {}, {}".format(number_1, number_2))

number_1, number_2 = number_2, number_1

print("\n Changing the order to {}, {}".format(number_1, number_2))



"""


Problem 6

Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2


"""

edge_a = int(input("Length of edge A is: "))
edge_b = int(input("Length of edge B is: "))

print("Calculating the hypotenuse...")

hypotenuse = (edge_a ** 2 + edge_b ** 2) ** 0.5

print("Hypotenuse is: ", hypotenuse)


