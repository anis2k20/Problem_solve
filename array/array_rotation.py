import operator
arr = [1, 2, 3, 4, 5, 6, 7]

d = 2
size = 7
sub_arr_1_len = size-d

sub_arr_1 = []
sub_arr_2 = []
rev_arr = list(reversed(arr))

for i in range(sub_arr_1_len):
    sub_arr_1.append(rev_arr[i])

for i in range(sub_arr_1_len,size):
    sub_arr_2.append(rev_arr[i])

sub_arr_1_rev = list(reversed(sub_arr_1))
sub_arr_2_rev = list(reversed(sub_arr_2))

total_arr = operator.add(sub_arr_1_rev,sub_arr_2_rev)
[print(item,end=" ") for item in total_arr]