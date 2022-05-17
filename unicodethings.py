
def FileOpen(filename=None):
    try:
        with open(filename, "r") as f:
            x = f.read()
            f.close()
            print(x)

    except OSError:
        # 'File not found' error message.
        print("OSError: File  not found")

    except TypeError:
        # theown if argument = None
        print('TypeError: No filename present.')


def test():
    FileOpen()
    FileOpen('pain.py')
    FileOpen('main.py')


if __name__ == '__main__':
    test()
