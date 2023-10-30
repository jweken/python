import lib.tuplethings as greet
import usererrors as error

greet
element = greet.Greeting()
print(greet.__doc__)
print(element)
print(type(greet))
print(type(greet.Greeting()))


def SquareBlock(num=None):
    print()
    squares = []
    if num == None:
        num = 10
    for x in range(num):
        squares.append(x*x)

    print(squares)


SquareBlock(100)
