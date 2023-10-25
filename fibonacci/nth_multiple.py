


def position(k,n):
    f0 = 0
    f1 = 1
    for i in range(2,10):
        f2 = f0+f1
        f0 = f1
        f1 = f2

        if f1%k==0:
            # print(i)
            return n*i

index = position(4,5)
# print(index)

a=0
b=1
for i in range(index-1):
    f=a+b
    a=b
    b=f
# print(f,end=" ")

print(f"{index}, fibonacci series is {f}")