import urllib.request
from bs4 import BeautifulSoup
import re

with open('seeds.txt') as fh:
    pages = fh.readlines()


output = open('output.html', 'w', encoding='UTF-8')
br = "<br>\n"
for p in pages:
    page = urllib.request.urlopen(p)
    html = str(page.read().decode('utf-8'))
    soup = BeautifulSoup(html, 'lxml')
    try:
        if (re.search('http', str(soup.img.get('src'))) == None):
            soup.img['src'] = p+soup.img['src']
    except:
        pass
    output.write("Título: ")
    output.write(str(soup.title.get_text()))
    output.write(br)
    output.write("Imagem: ")
    output.write(br)
    output.write(str(soup.img))
    output.write(br)
    output.write(br)
output.close()