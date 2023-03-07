from xml.dom.minidom import parse
import json

doc = parse('map.osm')

li = []

for node in doc.getElementsByTagName('node'):
    obj = dict()

    tags = node.getElementsByTagName('tag')
    for i in range(len(tags)):
        if (tags[i].getAttribute('k') == 'amenity') and ((i+1)<len(tags)):
            obj["type"] = "Feature"
            obj["geometry"]= dict(type="Point",coordinates= [float(node.getAttribute("lon")),float(node.getAttribute("lat"))])
            obj["properties"] = {
                "nome": tags[i+1].getAttribute("v"),
                "tipo": tags[i].getAttribute("v")
            }
            li.append(obj)

geojson = dict()
geojson["type"] = "FeatureCollection"
geojson["features"] = li

print(json.dumps(geojson, indent=4, ensure_ascii=False))