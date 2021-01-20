import os

def search_directory(path, tabspace):
    for name in os.listdir(path):
        name = os.path.join(path, name)
        if os.path.isdir(name):
            for i in range(tabspace):
                print('  ',end='')
            print(name)
            search_directory(name, tabspace+1)
        else:
            for i in range(tabspace-1):
                print('  ',end='')
            print(' -', end='')
            print(name)

# Enter the absolute path (not relative path!)
dir_name = input('Enter an address : ')

search_directory(dir_name, 0)