"""


EP6


"""


def f_div(num):

    full_div = []

    for i in range(2, num+1):

        if num % i == 0:
            full_div.append(i)

    return full_div


while True:
    num = input("Number:\n")

    if num.isalpha():
        print("\nCLOSING\n")
        break

    else:
        num = int(num)
        print("Full dividers: ", f_div(num))




