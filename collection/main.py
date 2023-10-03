def purchase(customer,size):
    customer_choice = {}
    for i in range(1,customer+1):
        s = int(input())
        p = int(input())
        if s in size:
            if s not in customer_choice:
                customer_choice.setdefault(f"{s}",[]).append(p)
            else:
                customer_choice.setdefault(f"{s}",[]).extend(p)
    print(customer_choice)


num_of_shoes = 10
available_size = [2,3,4,5,6,8,7,6,5,18]
num_of_customer = 6
purchase(num_of_customer,available_size)

