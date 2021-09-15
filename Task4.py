from sys import argv


def addelement(element, sizes):
    """return plural of variants which include element"""
    variants = set()
    for size in sizes:
        if element+size <= int(argv[1]):
            variants.add(element+size)
        variants.add(size)
    variants.add(element)
    return variants


variants = set()
for weight in argv[2:]:
    variants = addelement(int(weight), variants)
print(max(variants))
