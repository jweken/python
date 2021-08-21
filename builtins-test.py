import builtins


fd = builtins.open('greet.py', 'r')
content = fd.readlines()

for x in content:
    print(x, end='')
