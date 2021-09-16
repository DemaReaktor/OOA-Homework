from sys import argv
try:
    print(eval("".join(argv[1:]))) if not argv[2].isdigit() else exit()
except:
    print("error")
