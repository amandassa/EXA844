import urllib.request
from bs4 import BeautifulSoup

with open('seeds.txt') as fh:
    pages = fh.readlines()

for p in pages:
    page = urllib.request.urlopen(p)
    html = str(page.read().decode('utf-8'))
    soup = BeautifulSoup(html, 'lxml')

    print("Título:", soup.title.string)
    for img in soup.find_all('img'):
        print("src: ", img.attrs.get("src"))
        break