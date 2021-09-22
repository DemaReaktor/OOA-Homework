import operator
from sys import argv

try:
    print(operator.methodcaller(argv[1], int(argv[2]), int(argv[3]))(operator))
except:
    print("error")
