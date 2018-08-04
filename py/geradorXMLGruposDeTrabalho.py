# from xml.etree.ElementTree import Element,ElementTree
import re
import io
from py import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('grupos')
tree = et.ElementTree(root)
with open('../txt/GruposDeTrabalho.txt', encoding="utf8") as f:
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
            grupo = util.removeparenteses(line)
            gp = et.SubElement(root, "grupo")
            nome = et.SubElement(gp, "nome")
            nome.text = grupo.strip()
            for linha in res:
                ano = et.SubElement(gp, 'ano')
                ano.text = linha
        else:
            nomeparticipante = util.getnome(line)
            instituicao = util.get_instituicao(line)
            participante = et.SubElement(gp, "participante")
            participante.text = nomeparticipante.strip()
            if(instituicao != ""):
                inst = et.SubElement(gp, "instituicao")
                inst.text = instituicao.strip()



f.close()
#prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
#print(formatedXML)

#tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("../xml/GruposDeTrabalho2.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)


