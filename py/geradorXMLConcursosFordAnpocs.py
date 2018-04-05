# from xml.etree.ElementTree import Element,ElementTree
import re
import io
from py import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('ConcursosFordAnpocs')
tree = et.ElementTree(root)
with open('../txt/ConcursosFordAnpocs.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
    lines = clean_text.splitlines()

for line in lines:

    if not line or bool(re.match(r'\s\s*', line)):

        print("linha vazia")
    else:
        resano = re.search(r'\(\d\d\d\d\)', line)
        if bool(resano):
            anotxt = resano.group(0)
            continue
        vencedor = et.SubElement(root, "vencedor")
        nome = et.SubElement(vencedor, 'nome')
        txtnome = line.split(',')[0]
        nome.text = util.getnome(txtnome)
        res = re.search(r"(\d\d\d\d),?\s?(\d\d\d\d)?", line)
        if bool(res):
            ano = et.SubElement(vencedor, "ano")
            ano.text = res.group(1)
            if res.group(2) is not None:
                ano = et.SubElement(vencedor, "ano")
                ano.text = res.group(1)
        else:
            ano = et.SubElement(vencedor, "ano")
            ano.text = util.removeparenteses(anotxt)

f.close()
# prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
# print(formatedXML)

# tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("../xml/ConcursosFordAnpocs.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)


