"""

EP5

1,1,2,3,5,8,13,21,34....

"""

# a = 1 b = 1 output is 2 and so on...

a = 1
b = 1

fibonacci = [a, b]

for i in range(10):

    print("a: ", a, "b", b)

    a, b = b, a+b

    fibonacci.append(b)

print(fibonacci)












