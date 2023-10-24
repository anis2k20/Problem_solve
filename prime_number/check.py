num = int(input("Enter a digit: "))
is_prime = 1
for i in range(2,num):
    if num%i==0:
        is_prime = 0

if is_prime==1:
    print("Prime.")
else:
    print("Not prime.")