import builtins

#get the content of a file
def FileOpen(path=None):
    fd = builtins.open('greet.py', 'r')
    content = fd.readlines()

    for x in content:
        print(x, end='')

if __name__ == '__main__':
    FileOpen()
    
