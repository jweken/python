import builtins

# get the content of a file


def FileOpen(path=None):
    fd = builtins.open('lib/tuplethings.py', 'r')
    content = fd.readlines()

    for line in content:
        print(line, end='')


if __name__ == '__main__':
    FileOpen()
