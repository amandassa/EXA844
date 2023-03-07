import xml.sax

class OSMHandler (xml.sax.ContentHandler):
    def __init__(self):
        self.currentData = ''
        self.latitude = ''
        self.longitude = ''
        self.tipo = ''
        self.nome = ''
        self.isAmenity = False

    def startElement(self, tag, attrs):
        self.currentData = tag
        if tag == "node":
            self.latitude = attrs['lat']
            self.longitude = attrs['lon']
            # print(f'{self.latitude}, {self.longitude}')

        if tag == "tag":
            # se o atributo k=amenity então printe o atributo v
            if (attrs['k'] == 'amenity'):
                self.isAmenity = True
                self.tipo = attrs['v']
            if (attrs['k'] == 'name') and (self.isAmenity == True):
                self.nome = attrs['v']
                print(f'{self.nome},{self.tipo},{self.latitude},{self.longitude}')
    
    # def endElement(self, tag):
        # if tag == "node" and self.isAmenity == True:
        #     print(self.str)
            
if ( __name__ == "__main__"):
   parser = xml.sax.make_parser()
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

Handler = OSMHandler()
parser.setContentHandler( Handler )
parser.parse('map.osm')
