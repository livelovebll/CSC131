import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


a = int(input("Position: "))-1
b = int(input("Times: "))
url = "https://www.newegg.com/msi-geforce-rtx-2060-rtx-2060-ventus-gp-oc/p/N82E16814137695?Item=N82E16814137695"
for c in range(b):
    x = urllib.request.urlopen(url).read()
    y = BeautifulSoup(x, 'html.parser')
    z = y('a')
    d = z[a].get('href', None)
    url = d
    e = z[a].contents[0]

print(e)