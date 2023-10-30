""" 
This document is in module greet. 
If the greeting says otherwise, it is a lie.
"""

print('\nHi, I am main.py\n', end='')
print(f"file: {__file__}")


def TupleSample():
    """ TupleSample returns a tuple with three Literals"""
    x = "This is a text-item"
    y = "It can return a tuple of 3 items"
    z = 243
    return (x, y, z)


if __name__ == '__main__':
    print('\nResult of TupleSample()')
    print(TupleSample(), type(TupleSample()))
