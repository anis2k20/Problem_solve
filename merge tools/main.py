def merge_the_tools(string, k):
    l = len(string)

    for i in range(0,l,2):
        res = string[i:i+l]
        print(res)
        i=l

s = "AABCAAADA"
k=3
merge_the_tools(s,k)