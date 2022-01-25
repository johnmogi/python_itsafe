list = []
def collect(*args):
    if args is not None:
        for arg in args:
            list.append(arg)

collect(1,3,'g','pop')
print(list)