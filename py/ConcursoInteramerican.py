#from xml.etree.ElementTree import Element,ElementTree
import re
import io
from py import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('ConcursoInteramerican')
tree = et.ElementTree(root)
regex = r"([a-zA-Zà-úÀ-Ú\s\.]*),\s?(\d\d\d\d),?\s*(\d\d\d\d)?"
with open('../txt/ConcursoInteramerican.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)

matches = re.finditer(regex, txt)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    #print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        if groupNum == 1:
            vencedor = et.SubElement(root, "vencedor")
            nomeVencedor = et.SubElement(vencedor,"nomevencedor")
            nomeVencedor.text = match.group(groupNum)
        elif match.group is not None:
            ano = et.SubElement(root, "ano")
            ano.text = match.group(groupNum)



f.close()
# prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
# print(formatedXML)

# tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("../xml/ConcursosInteramerican.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)

