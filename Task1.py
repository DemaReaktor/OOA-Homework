from operator import *
from sys import argv
print({'+': add, '-': sub, '*': mul, '/': truediv}[argv[2]](int(argv[1]), int(argv[3])))
