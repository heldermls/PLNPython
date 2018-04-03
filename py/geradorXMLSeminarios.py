# from xml.etree.ElementTree import Element,ElementTree
import re
import io
from py import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('seminarios')
tree = et.ElementTree(root)
with open('../txt/SeminariosTematicos.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
    lines = clean_text.splitlines()


for line in lines:

    if not line or bool(re.match(r'\s\s*', line)):
        print("linha vazia")
    else:
        res = re.findall(r'\d\d\d\d', line)
        ehgrupo = bool(res)
        if(ehgrupo):
            smn = util.removeano(line)
            seminario = et.SubElement(root, "seminario")
            nome = et.SubElement(seminario, "nome")
            nome.text = smn.strip()
            for linha in res:
                ano = et.SubElement(seminario, 'ano')
                ano.text = linha
        else:
            nomeparticipante = util.getnome(line)
            instituicao = util.get_instituicao(line)
            participante = et.SubElement(seminario, "participante")
            participante.text = nomeparticipante.strip()
            if(instituicao != ""):
                inst = et.SubElement(participante, "instituicao")
                inst.text = instituicao.strip()



f.close()
#prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
#print(formatedXML)

#tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("../xml/Seminarios.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)


