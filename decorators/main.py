# def apply(func,value):
#     return func(value)
#
# def square(x):
#     return x**2
#
# result = apply(square,5)
#
# print(result)

def attach_data(func):
    func.data = 3
    return func

@attach_data
def add(x,y):
    return x+y

print(add(2,3))
print(add.data)