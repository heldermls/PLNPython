# from xml.etree.ElementTree import Element,ElementTree
import re
import io
import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('programas')
tree = et.ElementTree(root)
with open('Programas.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
    lines = clean_text.splitlines()


for line in lines:
    # if its a break of subelements  - that is an empty space

    if not line:
        # add the next subelement and get it as celldata
        # bienio = ET.SubElement(root, 'bienios')
        print("linha vazia")
    else:
        ehprograma = bool(re.search('\(|\)', line))
        ehestado = not ehprograma
        estado = util.getnome(line)

        if ehprograma:
            print(line)
            res = line.split(",")
            programa = res[0]
            strano = res[-1]

            nomeinstituicao = util.get_instituicao(programa)
            programa = programa.replace(nomeinstituicao, "")
            programa = programa.replace("(", "")
            programa = programa.replace(")", "")

            prg = et.SubElement(root, "programa")
            nomeprograma = et.SubElement(prg, 'nomeprograma')
            nomeprograma.text = programa.strip()

            instituicao = et.SubElement(prg, 'instituicao')
            instituicao.text = nomeinstituicao
            print(strano)
            res = re.search(r'\d\d\d\d',strano)
            anofiliacao = res[0]

            anofili = et.SubElement(prg, 'anofiliacao')
            anofili.text = anofiliacao



f.close()
#prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
#print(formatedXML)

#tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("Programas.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)


