# Python program to print all Prime numbers in an Interval

num = 100
prime_nums=[]

for i in range(2,num+1):
    if i>=2:
        flag=0
        for j in range(2,i):
           if i%j==0:
               flag=1
        if flag==0:
            prime_nums.append(i)

print(prime_nums)
