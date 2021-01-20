my_list = [9,8,7,6,5,4,3,2,1,0]

def binary_search(a_list, search_no):
    a_list.sort()
    print(a_list)
    f = 0
    l = len(a_list)
    m = (f+l)//2

    while m>=f and m<l:
        if a_list[m] == search_no:
            return m
        elif a_list[m] < search_no:
            f = m
            m = (f+l)//2
        else:
            l = m
            m = (f+l)//2
    return -1

search_no = 2
print("Search number : "+str(search_no))
print("At index : " + str(binary_search(my_list, search_no)))