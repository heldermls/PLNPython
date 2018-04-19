import re
import io
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('AutoresRBCS')
tree = et.ElementTree(root)
regex = r"([\w\s,;\-&’]*)\.\s([\?!\:\w\s,\(\)\"\-\d&\/]*).\s*RBCS\s(nº)?\s(\d+),\s*(\w\w\w)?\s(\d\d\d\d)\s"
with open('../txt/AutoresRBCS.txt', encoding='utf-16') as f:
    txt = f.read()
matches = re.finditer(regex, txt)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    obra = et.SubElement(root, "obra")

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        if groupNum == 1:
            autores = re.split("\se\s|;", match.group(groupNum))
            for nome in autores:
                print(nome)
                nomes = nome.split(",")
                autor = et.SubElement(obra, "autor")
                nomeautor = et.SubElement(autor, "nomeautor")
                nomeautor.text = (nomes[1] + " " + nomes[0]).strip()
        if groupNum == 2:
            nomeobra = et.SubElement(obra, "publicacao")
            nomeobra.text = match.group(groupNum).strip()

        if groupNum == 4:
            if match.group(groupNum) != " ":
                edicao = et.SubElement(obra, "numeroedicao")
                edicao.text = match.group(groupNum).strip()
        if groupNum == 5:
            if match.group(groupNum) != 0000:
                ano = et.SubElement(obra, "mes")
                ano.text = match.group(groupNum)
        if groupNum == 6:
            if match.group(groupNum) != 0000:
                ano = et.SubElement(obra, "ano")
                ano.text = match.group(groupNum)
f.close()
formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
with io.open("../xml/AutoresRBCS.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)
