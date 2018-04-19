import re
import io
from py import util_strings as util
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et
import html.parser
html_parser = html.parser.HTMLParser()

root = et.Element('Homenageados')
tree = et.ElementTree(root)
regex = r"([^a-z]*\s)([\w\s]*(BIB|RBCS)\s(\d\d).*(\d\d\d\d),.*)?"
with open('../txt/Homenagens.txt', encoding='utf-8') as f:
    txt = f.read()
    #clean_text = unicodedata.normalize("NFKD", txt)
    #print(clean_text)

matches = re.finditer(regex, txt)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    homenageado = et.SubElement(root, "homenageado")
    #print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        #print(match.group(groupNum), groupNum)
        if groupNum == 1:
            nomeautor = et.SubElement(homenageado, "nome")
            nomeautor.text = match.group(groupNum).strip()

        if groupNum == 3:
            revista = et.SubElement(homenageado, "revista")
            nomerevista = et.SubElement(revista, "nomerevista")
            nomerevista.text = match.group(groupNum).strip()

        if groupNum == 4:
           edicao = et.SubElement(revista, "numeroedicao")
           edicao.text = match.group(groupNum).strip()
        if groupNum == 6:
            if match.group(groupNum) != 0000:
                ano = et.SubElement(revista, "ano")
                ano.text = match.group(groupNum)



f.close()
# prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
# print(formatedXML)

# tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("../xml/Homenageados.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)

