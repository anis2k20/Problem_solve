def purchase(customer,size):
    customer_choice = {}
    # customer_choice = {'6': [55, 45, 55], '4': [40], '18': [60]}
    output = 0
    for i in range(1,customer+1):
        s = int(input())
        p = int(input())
        if s in size:
            if s not in customer_choice:
                customer_choice.setdefault(f"{s}",[]).append(p)
            else:
                customer_choice.setdefault(f"{s}",[]).extend(p)

    cus_selection = customer_choice.keys()
    cus_selection_dict = {}
    for i in cus_selection:
        cus_selection_dict[i]=size.count(int(i))

    l = []
    for i in cus_selection_dict.values():
        l.append(i)

    x=0
    for i in customer_choice.values():
        for j in range(l[x]):
            output+=i[j]
        x+=1

    print(output)


num_of_shoes = 10
available_size = [2,3,4,5,6,8,7,6,5,18]
num_of_customer = 6
purchase(num_of_customer,available_size)

