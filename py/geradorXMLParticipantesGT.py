#from xml.etree.ElementTree import Element,ElementTree
import re
import io
from py import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('ParticipantesGT')
tree = et.ElementTree(root)
regex = r"(([a-zA-Zá-úÁ-Ú]|\s|\’|\-)*)(\(([a-zA-Zá-úÁ-Ú]+(\/|\-)?([a-zA-Zá-úÁ-Ú\s]*)?).)?\n"
with open('../txt/ParticipantesGT.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)

matches = re.finditer(regex, txt)
nomeInstituicao =""
for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    #print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(), end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        #print(match.group(4))
        if groupNum == 1 and match.group(groupNum) != None and match.group(groupNum) !="" :
            participante = et.SubElement(root, "participante")
            nome = et.SubElement(participante,"nome")

            nome.text = match.group(groupNum).strip()
        if groupNum == 4 and match.group(groupNum) != None and match.group(groupNum) !="" :
            instituicao = et.SubElement(participante, "instituicao")
            instituicao.text = match.group(groupNum).strip()





f.close()
# prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
# print(formatedXML)

# tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("../xml/ParticipantesGT.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)

