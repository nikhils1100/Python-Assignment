import random

class ReverseIter():
    def __init__(self, list_):
        self.list_ = list_

    def __iter__(self):
        self.index = self.__len__()-1
        return self

    def __next__(self):
        if self.index >=0:
            result = self.list_[self.index]
            self.index -= 1
            return result
        else:
            raise StopIteration

    def __len__(self):
        return len(self.list_)

n = 10
my_list = []

# Randomly generating n integers
for i in range(n):
    my_list.append(random.randint(0,n))

print("Original : ")
for i in my_list:
    print(i, end=', ')
print()

my_list_rev = ReverseIter(my_list)
my_list_rev = iter(my_list_rev)

print("Reversed : ")
for i in my_list_rev:
    print(i, end=', ')
print()