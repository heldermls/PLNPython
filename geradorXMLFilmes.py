# from xml.etree.ElementTree import Element,ElementTree
import re
import io
import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('filmes')
tree = et.ElementTree(root)
with open('Filmes.txt', encoding="utf8") as f:
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
        strfilme = line.replace(spl[0] + ',', "")
        resfilme = strfilme.split("#")
        partic = et.SubElement(root, "participante")
        nomeparticipante = et.SubElement(partic, "nome")
        nomeparticipante.text = util.getnome(strnome)
        if nomeinstituicao != "":
            instituicao = et.SubElement(partic, 'instituicao')
            instituicao.text = nomeinstituicao
        for filme in resfilme:
            fm = et.SubElement(partic, "filme")
            ennome = et.SubElement(fm, "nome")

            res = re.search(r'\s\d\d\d\d\s', filme)
            if res is not None:
                ano = res.group(0)
                filme = filme.replace(ano, "")
                year = et.SubElement(fm, "ano")
                year.text = ano.strip()
            ennome.text = filme.strip()



f.close()
#prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
#print(formatedXML)

#tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("Filmes.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)


