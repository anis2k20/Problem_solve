n = input("Enter number: ")
l=[]
for i in n:
    temp=pow(int(i),3)
    l.append(temp)

s = sum(l)
if s==int(n):
    print("This number is armstrong.")
else:
    print("This number is not armstrong.")

