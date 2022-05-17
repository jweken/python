import greet
import usererrors as error

greet
element = greet.Greeting()
print(greet.__doc__)
print(element)
print(element[0])
print(element[2])
print(type(greet))
print(type(greet.Greeting()))
print(type(element[2]))

squares = []
for x in range(100):
    squares.append(x*x)

print(squares)
