import os, sys

def get_dir():
    for i in range(1, 10):
        new_dir = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.mkdir(new_dir)

def del_dir():
    for i in range(1, 10):
        new_dir = os.path.join(os.getcwd(), 'dir_{}'.format(i))
        os.rmdir(new_dir)

command = sys.argv[1]
if command == 'get':
    get_dir()
    print('Папки созданы')
elif command == 'delet':
    del_dir()
    print('Папки удалены')