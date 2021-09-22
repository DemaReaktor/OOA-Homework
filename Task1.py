from sys import argv
from operator import *

try:
    print({'+': add, '-': sub, '*': mul, '/': truediv}[argv[2]](int(argv[1]), int(argv[3])))
except:
    print("error")
