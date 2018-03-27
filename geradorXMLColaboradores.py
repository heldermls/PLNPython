# from xml.etree.ElementTree import Element,ElementTree
import re
import io
import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('colaboradores')
tree = et.ElementTree(root)
with open('Colaboradores.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
    lines = clean_text.splitlines()


for line in lines:
    # if its a break of subelements  - that is an empty space

    if not line or bool(re.match(r'\s\s*', line)):
        # add the next subelement and get it as celldata
        # bienio = ET.SubElement(root, 'bienios')
        print("linha vazia")
    else:

        colaborador = et.SubElement(root, "colaborador")
        nome = et.SubElement(colaborador, 'nome')
        nome.text = util.getnome(line)


f.close()
#prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
#print(formatedXML)

#tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("Colaboradores.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)


