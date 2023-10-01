def calculate(l1, l2):
    l = []
    for i in l1:
        if i!=" ":
            for j in l2:
                if j!=" ":
                    l.append((int(i),int(j)))

    for i in l:
        print(i,end="")
l1 = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14"
l2 = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14"
calculate(l1, l2)