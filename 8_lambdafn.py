my_list = []
for i in range(1,21):
    my_list.append(i)

my_list = list(map(lambda x:x*x, my_list))

print(my_list)