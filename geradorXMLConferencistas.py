# from xml.etree.ElementTree import Element,ElementTree
import re
import io
import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('conferencistas')
tree = et.ElementTree(root)
with open('Conferencistas.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
    lines = clean_text.splitlines()


for line in lines:
    # if its a break of subelements  - that is an empty space

    if not line or bool(re.match(r'\s\s*', line)):
        # add the next subelement and get it as celldata
        # bienio = ET.SubElement(root, 'bienios')
        print("linha vazia")
    else:
        spl = line.split(',')
        strnome = spl[0]
        nomeinstituicao = util.get_instituicao(strnome)
        strnome = util.removeparenteses(strnome.replace(nomeinstituicao, ""))
        strconf = line.replace(spl[0]+',', "")
        resconf = strconf.split("#")
        conferencista = et.SubElement(root, "conferencista")
        nome = et.SubElement(conferencista, 'nome')
        nome.text = util.getnome(strnome)
        instituicao = et.SubElement(conferencista, 'instituicao')
        instituicao.text = nomeinstituicao
        for conf in resconf:
            ano = re.search(r'\d\d\d\d', conf).group(0)
            conf = conf.replace(ano, "")
            conferencia = et.SubElement(conferencista, "conferencia")
            conferencia.text = conf.strip()
            year = et.SubElement(conferencia, "ano")
            year.text = ano

f.close()
#prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
#print(formatedXML)

#tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("Conferencistas.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)


