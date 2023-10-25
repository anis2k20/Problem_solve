#n-th fibonacci number (1 1 2 3 5 8 13..........)
n=10

a=0
b=1
print(a,b,end=" ")
for i in range(n-2):
    fibbo = a+b
    a = b
    b = fibbo
    print(fibbo,end=" ")