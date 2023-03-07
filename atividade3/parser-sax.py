import xml.sax

class OSMHandler (xml.sax.ContentHandler):
    def __init__(self):
        self.currentData = ''
        self.latitude = ''
        self.longitude = ''
        self.tipo = ''
        self.nome = ''
        self.str = ''
        self.isAmenity = False

    def startElement(self, tag, attrs):
        self.currentData = tag
        if tag == "node":  
            self.latitude = attrs['lat']
            self.longitude = attrs['lon']
            self.str += f'Latitude: {self.latitude:^10}\tLongitude: {self.longitude:^10}\t'

        if tag == "tag":
            # se o atributo k=amenity então printe o atributo v
            if (attrs['k'] == 'amenity'):
                self.isAmenity = True
                self.tipo = attrs['v']                
            if (attrs['k'] == 'name'):
                self.nome = attrs['v']
            self.str += f'Tipo: {self.tipo:^10}\tNome: {self.nome:^10}\t'

    
    def endElement(self, tag):
        if tag == "node" and self.isAmenity == True:
            print(self.str)
            
if ( __name__ == "__main__"):
   parser = xml.sax.make_parser()
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

Handler = OSMHandler()
parser.setContentHandler( Handler )
parser.parse('map.osm')
