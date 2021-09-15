from sys import argv


def isExpression(text):
    for number in text.replace('-', '+').split('+'):
        if not number.isdigit():
            return 0
    return text[0].isdigit() and text[-1].isdigit()


print("(True,{0})".format(eval(argv[1])) if isExpression(argv[1]) else "(False,None)")
