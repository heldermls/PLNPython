# from xml.etree.ElementTree import Element,ElementTree
import re
import io
from py import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('participantes')
tree = et.ElementTree(root)
with open('../txt/Participantes.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
    lines = clean_text.splitlines()


for line in lines:

    if not line or bool(re.match(r'\s\s*', line)):
        print("linha vazia")
    else:
        line = util.explodeperiodo(line)
        res = re.search(r'(\D|\s)+', line)
        print(line)
        participante = et.SubElement(root, "participante")
        nome = et.SubElement(participante, "nome")
        nome.text = res[0].strip()
        txtanos = ""
        anos = re.findall(r'\d\d\d\d', line)
        for ano in anos:
            txtanos = txtanos + ";" + ano
        anos = et.SubElement(participante, "anos")
        anos.text = txtanos.split(";", 1)[-1]
f.close()
#prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
#print(formatedXML)

#tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("../xml/Participantes2.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)


