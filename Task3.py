from _operator import add, sub
from sys import argv


def formula(text, number=""):
    """method convert text into expression and return value"""
    if text.isdigit():
        return int(text)
    if (text[0] == '+' or text[0] == '-') and number and text[1:]:
        return sign(text[0], number, text[1:len(text)])
    if text[0].isdigit():
        return formula(text[1:len(text)], number+text[0])


def sign(operator, text1, text2):
    """method do operation(sum or subtract) with values of texts"""
    if formula(text2):
        return {'+': add, '-': sub}[operator](formula(text1), formula(text2))


result = formula(argv[1])
print("(True,{0})".format(result) if result else "(False,None)")
