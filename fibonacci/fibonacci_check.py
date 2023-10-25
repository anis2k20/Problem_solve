user_input = input("Enter your number seriese: ")
num = user_input.split()

# check
flag = 0
for i in range(len(num)-2):
    if int(num[i])+int(num[i+1]) != int(num[i+2]):
        flag = 1
        break

if flag == 0:
    print("It's a fibonacci seriese.")
else:
    print("It's not a fobonacci seriese.")