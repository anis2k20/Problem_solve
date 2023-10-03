from itertools import product


def calculate(a, b):
    l1 = []
    l2 = []
    for i in a:
        if i != " ":
            l1.append(int(i))
    for i in b:
        if i != " ":
            l2.append(int(i))

    l = product(l1, l2)
    for i in l:
        print(i,end=" ")


a = "1 2"
b = "3 4"
calculate(a, b)