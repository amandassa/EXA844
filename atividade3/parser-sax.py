import xml.sax
import time as t


class OSMHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.inNode = ""
        self.latitude = ""
        self.longitude = ""
        self.tipo = ""
        self.value = ""
        self.nome = ""

    def startElement(self, tag, attrs):
        if tag != "node" and tag != "tag":
            return
        if tag == "node":
            self.latitude = attrs.get("lat")
            self.longitude = attrs.get("lon")
            self.inNode = True
            return
        if not self.inNode:
            return
        self.value = attrs.get("v")
        key = attrs.get("k")
        if key == "amenity":
            self.tipo = self.value
        elif key == "name":
            self.nome = self.value

    def endElement(self, tag):
        if tag != "node":
            return

        if self.tipo != "":
            print(f'Nome: {self.nome:<10}\tTipo: {self.tipo:<10}\tLat: {self.latitude:^10}\tLon: {self.longitude:^10}')
        self.__resetVariables()

    def __resetVariables(self):
        self.inNode = ""
        self.latitude = ""
        self.longitude = ""
        self.tipo = ""
        self.value = ""
        self.canPrint = False


start = t.time()
parser = xml.sax.make_parser()
Handler = OSMHandler()
parser.setContentHandler(Handler)
parser.parse("map.osm")
seconds = t.time() - start
print("A execução levou {:.2f} segundos.".format(seconds))
