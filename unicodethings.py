line80 = str('_'*80)
dashline80 = str('-'*80)
slashes80 = str('/'*80)


def SlashJines(num=None):
    if num == None:
        print(slashes80)

    else:
        for i in range(num):
            print(slashes80)


def FileOpen(filename=None):
    print(line80)
    try:
        with open(filename, "r") as handle:
            x = handle.read()
            handle.close()
            print(x)

    except OSError:
        # 'File not found' error message.
        print("OSError: File  not found")

    except TypeError:
        # theown if argument = None
        print('TypeError: No filename present.')

    SlashJines(3)


def test():
    FileOpen()
    FileOpen('pain.py')
    FileOpen('main.py')


if __name__ == '__main__':
    test()
