# Python program to print all Prime numbers in an Interval

num = 12
prime_nums=[]

for i in range(1,num+1):
    if i>=3:
        for j in range(2,i):
            if i%j==0:
                print("not prime")
                continue
            else:
                prime_nums.append(i)

print(prime_nums)