# from xml.etree.ElementTree import Element,ElementTree
import re
import io
from py import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et
nomerevista = ""
root = et.Element('Pareceristas')
tree = et.ElementTree(root)
with open('../txt/Pareceristas.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
    lines = clean_text.splitlines()


for line in lines:

    if not line or bool(re.match(r'\s\s*', line)):
        print("linha vazia")
    else:

        resline = re.search(r'RBCS|BIB', line)
        isrevista = bool(resline)
        if isrevista:
            nomerevista = resline.group(0)
        parecerista = et.SubElement(root, "parecerista")
        nome = et.SubElement(parecerista, 'nome')
        nome.text = util.getnome(line)
        revista = et.SubElement(parecerista, "revista")
        revista.text = nomerevista


f.close()
#prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
#print(formatedXML)

#tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("../xml/Pareceristas.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)


