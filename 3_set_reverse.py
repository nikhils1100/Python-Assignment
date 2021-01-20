from collections import deque

my_list =  [12,24,35,24,88,120,155,88,120,155]
order = 'maintain'

if order=='not maintain':
    my_list_len = len(my_list)

    for i in range(0,int(my_list_len/2)):
        tmp = my_list[i]
        my_list[i] = my_list[my_list_len-i-1]
        my_list[my_list_len-i-1] = tmp

    print(my_list)

else:
    stack_list = deque()
    buff = {} # Hashmap for better search time

    # Check if each element is in buff or not
    for i in range(len(my_list)):
        if my_list[i] not in buff:
            buff[my_list[i]] = 0
            stack_list.append(my_list[i])

    my_list = []
    for i in range(len(stack_list)):
        my_list.append(stack_list.pop())
    
    print(my_list)