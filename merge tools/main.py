def merge_the_tools(string, k):
    l = len(string)
    string_list = []
    for i in range(0,l,k):
        res = string[i:i+k]
        temp = ""
        for j in res:
            if j not in temp:
                temp+=j
        string_list.append(temp)
    for i in string_list:
        print(i)


s = "AABCAAADA"
k=3
merge_the_tools(s,k)