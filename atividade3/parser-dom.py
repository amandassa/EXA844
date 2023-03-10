from xml.dom.minidom import parse
import time as t

doc = parse('map.osm')

for node in doc.getElementsByTagName('node'):
    tags = node.getElementsByTagName('tag')
    for i in range(len(tags)):
        if (tags[i].getAttribute('k') == 'amenity') and ((i+1)<len(tags)):
            print(f'Nome: {tags[i+1].getAttribute("v") : ^10} \t Tipo: {tags[i].getAttribute("v"): <10} \t Lat: {node.getAttribute("lat"): ^10} \t Lon: {node.getAttribute("lon"):^10}')

start = t.time()
seconds = t.time() - start
print("A execução levou {:.2f} segundos.".format(seconds))
