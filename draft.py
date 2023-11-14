# Prime check----------------
# def prime_check(num):
#     if num in [2,3]:
#         return True
#     elif num==1 or num%2==0:
#         return False
#     else:
#         r = 3
#         while r<num:
#             if num%r==0:
#                 return False
#                 r += 2
#             else:
#                 return True
#
# print(prime_check(76))

# def check(**args):
#     for key,value in args.items():
#         print("%s : %s" % (key,value))
#
# check(name="anis", roll="190",email="anis@gmail.com")

class MyClass:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


# Create an instance of MyClass
obj = MyClass(10)

# Call the get_value method on the instance
print(obj.get_value())  # Output: 10