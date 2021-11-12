import timeit

s = """with open('f.json', 'r') as file_r:
        s = 0
        for line in file_r:
            if line.strip().isdigit():
                s += int(line.strip())"""
print(timeit.timeit(s))

s = """with open('f.json', 'r') as file_r:
        s = 0
        for line in file_r:
            if line.strip().isdigit():
                s += int(line.strip())
        print(s)"""
print(timeit.timeit(s))

s = """
with open('f.json', 'r') as file_r:
    s = 0
    s += [int(line.strip()) for line in file_r if line.strip().isdigit()]
    print(s)
        """
print(timeit.timeit(s))
