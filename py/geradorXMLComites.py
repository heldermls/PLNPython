# from xml.etree.ElementTree import Element,ElementTree
import re
import io
from py import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('comissoes')
tree = et.ElementTree(root)
with open('../txt/Comites.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
    lines = clean_text.splitlines()


for line in lines:

    if not line or bool(re.match(r'\s\s*', line)):
        print("linha vazia")
    else:

        anos = re.findall('\d\d\d\d', line)
        search = re.search('Comit.*|Comiss.*|Pr.mio.*|Conse.*|J.*ri.*', line)
        ehcomite = bool(search)
        ehnome = (not ehcomite) and (not bool(anos))
        if bool(anos):
            if len(anos) == 2:
                ano_1 = anos[0]
                ano_2 = anos[1]
            if len(anos) == 1:
                ano_1 = anos[0]
                ano_2 = ""
        if ehcomite:
            cmt = line

        if ehnome:
            participante = et.SubElement(root, "participante")
            nome = et.SubElement(participante, 'nome')
            nome.text = util.getnome(line)
            nomeinstituicao = util.get_instituicao(line)
            if nomeinstituicao != "":
                instituicao = et.SubElement(participante, 'instituicao')
                instituicao.text = nomeinstituicao
            comite = et.SubElement(participante, 'comite')
            nomecomite = et.SubElement(comite, 'nomecomite')
            nomecomite.text = cmt.strip()
            anoI = et.SubElement(comite, 'ano')
            anoI.text = ano_1
            if (ano_2 != ""):
                anoF = et.SubElement(comite, 'ano')
                anoF.text = ano_2


f.close()
#prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
#print(formatedXML)

#tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("../xml/Comissoes.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)


