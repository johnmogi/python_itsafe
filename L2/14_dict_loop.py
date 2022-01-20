books = {
    "fiction":"Hobbit",
    "fantasy":"LOTR",
    "Horror":"The dark tower",
    "sci fi":"dune",
    }

# for key in books.keys() :
#     # print (key)
#     print (books[key])

# for value in books.values() :
#     print (value)

for key,value in books.items() :
    print(key,':',value)
    