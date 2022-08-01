

def sort(sort_num):
    for i in range(len(sort_num)-1,0,-1):
        for j in range(i):
            if sort_num(j) > sort_num(j+1):
                temp = sort_num(j)
                sort_num(j) == sort_num(j+1)
                sort_num(j+1) == temp



sort_num = [3, 2, 5, 8, 7]
sort(sort_num)
print(sort_num)