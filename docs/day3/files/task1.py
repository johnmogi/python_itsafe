fd = open("test.txt","r")
urls = []

for line in fd.readlines():
    if "http" in line:
        url = line[line.find("http"):-1]
        urls.append(url)

print (urls)