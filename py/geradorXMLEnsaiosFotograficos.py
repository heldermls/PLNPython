# from xml.etree.ElementTree import Element,ElementTree
import re
import io
from py import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('ensaiosfotograficos')
tree = et.ElementTree(root)
with open('../txt/EnsaiosFotograficos.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
    lines = clean_text.splitlines()


for line in lines:

    if not line or bool(re.match(r'\s\s*', line)):
        print("linha vazia")
    else:
        spl = line.split(',')
        strnome = spl[0]
        nomeinstituicao = util.get_instituicao(strnome)
        strnome = util.removeparenteses(strnome.replace(nomeinstituicao, ""))
        strensaio = line.replace(spl[0]+',', "")
        resen = strensaio.split("#")
        partic = et.SubElement(root, "participante")
        nomeparticipante = et.SubElement(partic, "nome")
        nomeparticipante.text = util.getnome(strnome)
        if nomeinstituicao != "":
            instituicao = et.SubElement(partic, 'instituicao')
            instituicao.text = nomeinstituicao
        for ensaio in resen:
            en = et.SubElement(partic, "ensaio")
            ennome = et.SubElement(en, "nome")

            res = re.search(r'\s\d\d\d\d\s', ensaio)
            if res is not None:
                ano = res.group(0)
                ens = ensaio.replace(ano, "")
                year = et.SubElement(en, "ano")
                year.text = ano.strip()
            ennome.text = ens.strip()



f.close()
#prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
#print(formatedXML)

#tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("../xml/EnsaiosFotograficos.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)


