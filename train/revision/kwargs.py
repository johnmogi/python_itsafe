list = []

def dict(**kwargs):
    if 'name' in kwargs.keys():
        print(kwargs["name"])


#        list.append(k)

dict(name = 'john', age = 43)

for i in list:
    print(i)
