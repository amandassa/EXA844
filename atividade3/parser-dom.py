from xml.dom.minidom import parse

doc = parse('map.osm')

for node in doc.getElementsByTagName('node'):
    # print(node.getAttribute('lat'))
    for tag in node.getElementsByTagName('tag'):
        if (tag.getAttribute('k') == 'amenity'):
            print(f'Nome: {"#TODO": ^10} \t Tipo: {tag.getAttribute("v"): <10} \t Lat: {node.getAttribute("lat"): ^10} \t Lon: {node.getAttribute("lon"):^10}')