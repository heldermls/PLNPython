#from xml.etree.ElementTree import Element,ElementTree
import re
import io
from py import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('ConcursoPaineis')
tree = et.ElementTree(root)
regex = r"(([a-zA-Zá-úÁ-Ú]|\s)*)(\(.*\)),\s*(\d\d\d\d)(.*)\n"
with open('../txt/ConcursoPaineis.txt', encoding="utf8") as f:
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
            nomeVencedor.text = match.group(groupNum).strip()
        if groupNum == 3:
            instituicao = et.SubElement(vencedor,"instituicao")
            instituicao.text = util.removeparenteses(match.group(groupNum))
        if groupNum == 4:
            ano = et.SubElement(vencedor, "ano")
            ano.text = match.group(groupNum)
        if groupNum == 5:
            painel = et.SubElement(vencedor, "painel")
            painel.text = match.group(groupNum).strip()



f.close()
# prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
# print(formatedXML)

# tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("../xml/ConcursoPaineis.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)

