"""

Proje 1

Math modülündeki hazır fonksiyonları kullanarak gelişmiş bir hesap makinesi geliştirmeye çalışın.



Proje 2

Math modülünde kullandığınız fonksiyonları kendiniz de ayrı bir modüle (Python dosyasına) yazmaya çalışın ve bu yazdığınız modülü kullanarak gelişmiş bir hesap makinesi yazın.



"""

"""
https://docs.python.org/3/library/math.html
"""

import math
import time

func = input("""
Select a function you wish to calculate:\n

1 - Ceil
2 - Floor
3 - Factorial
4 - Absolute Value
5 - Log
6 - Square Root


""")


def calculator():

    while True:

        if func.isalpha():
            print("\nCLOSING\n.")
            break

        if func == 1:

            print("Returns the ceiling of x, the smallest integer greater than or equal to x.\n")

            number = float(input("Number:\n"))

            print("Ceiling of the number {}:\n".format(number), math.ceil(number))

            if number.is_integer():

                print("""\n
                ***********************
                Input needs to be float
                ***********************\n
                """)

                calculator()

        if func == 2:

            print("Returns the floor of x, the largest integer less than or equal to x. ")

            number = float(input("Number:\n"))

            print("Floor of the number {}:\n".format(number), math.floor(number))

            if number.is_integer():

                print("""\n
                ***********************
                Input needs to be float
                ***********************\n
                """)

                calculator()

        if func == 3:

            print("Returns 'x' factorial.")

            number = int(input("Number:\n"))

            print("Factorial of the number {}:\n".format(number), math.factorial(number))

            if isinstance(number, float):

                print("""\n
                *************************
                Input needs to be integer
                *************************\n
                """)

                calculator()

        if func == 4:

            print("Returns the absolute value of x.")

            number = float(input("Number:\n"))

            print("Absolute value of the number {}:\n".format(number), math.fabs(number))

        if func == 5:

            print("With one argument, returns the natural logarithm of x (to base e).\nWith two arguments, returns the logarithm of x to the given base, calculated as log(x)/log(base).")

            number = int(input("Number:\n"))

            question = str(input("Do you want to input a base?\n(Y or N)\n"))

            if question == "y":
                base = int(input("Base:\n"))
                print("Calculating...\n")
                time.sleep(1)

                print("\nLog {} with base {} is:\n".format(number, base), math.log(number, base))

            else:
                print("\nLog {} is:\n".format(number), math.log(number))

        if func == 6:

            print("Returns the square root of x.")

            number = int(input("Number:\n"))

            print("Square root of {} is:\n".format(number), math.sqrt(number))

            if isinstance(number, float):

                print("""\n
                *************************
                Input needs to be integer
                *************************\n
                """)

                calculator()



calculator()
