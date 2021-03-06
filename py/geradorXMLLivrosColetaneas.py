import re
import io
from py import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et
root = et.Element('LivrosColetaneas')
tree = et.ElementTree(root)
regex = r"(([a-zA-Zá-úÁ-Ú.\(\)-]|\s?)*),(.*),(.*),.*(\d\d\d\d).*\n"
with open('../txt/LivrosColetaneas.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
matches = re.finditer(regex, txt)
for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1
    obra = et.SubElement(root, "obra")
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        if groupNum == 1:
            vencedores = match.group(groupNum).split(" e ")
            for nome in vencedores:
                print(nome)
                res = re.search(r'\(.*\)', nome)
                txtnome = nome
                autor = et.SubElement(obra, "autor")
                nomeautor = et.SubElement(autor, "nomeautor")
                if bool(res):

                    txtnome = txtnome.replace(res[0], "")
                    funcao = et.SubElement(autor, "funcao")
                    if res.group(0).__contains__("oo"):
                        funcao.text = "coordenador"
                    else:
                        funcao.text = "organizador"
                nomeautor.text = txtnome
        if groupNum == 3:
            nomeobra = et.SubElement(obra, "nomeobra")
            nomeobra.text = match.group(groupNum).strip()
        if groupNum == 4:
            if match.group(groupNum) != " ":
                editora = et.SubElement(obra, "editora")
                editora.text = match.group(groupNum).strip()
        if groupNum == 5:
            if match.group(groupNum) != 0000:
                ano = et.SubElement(obra, "ano")
                ano.text = match.group(groupNum)
f.close()
formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
with io.open("../xml/LivrosColetaneas.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)

