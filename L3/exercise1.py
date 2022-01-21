fd = open('README.md.txt','r')
urls = []
lines = fd.readlines()
for line in lines:
    if 'http' in line:
        url = line[line.find("http"):-1]
        urls.append(url)
print(urls)
fd.close()