"""


EP6


"""


def prime(num):

    if num == 1:
        return False

    elif num == 2:
        return True

    else:
        for i in range(2, num):

            if num % i == 0:
                return False

        return True


while True:
    num = input("Number:\n")

    if num.isalpha():
        print("\nClosing.\n")
        break

    else:
        num = int(num)

        if prime(num):
            print("Number {} is prime".format(num))

        else:
            print("Number {} is NOT prime".format(num))



