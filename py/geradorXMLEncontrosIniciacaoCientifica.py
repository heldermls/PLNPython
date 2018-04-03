# from xml.etree.ElementTree import Element,ElementTree
import re
import io
from py import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('encontros')
tree = et.ElementTree(root)
anos = [0, 0]
with open('../txt/EncontrosIniciacaoCientifica.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
    lines = clean_text.splitlines()
#gerando iterador para ter acesso ao next()
itr = iter(lines)
for line in itr:

    if not line or bool(re.match(r'\s\s*', line)):
        print("linha vazia")
    else:


        searchpapel = re.search(r'Autores.*|Coordenadores.*|Comiss.*', line)
        ehcargo = bool(searchpapel)

        if ehcargo:
            papel = searchpapel.group(0)
            papel = papel.replace("Autores com trabalhos aprovados:", "Autor com trabalho aprovado")
            papel = papel.replace("Coordenadores:", "Coordenação")
            print(searchpapel.group(0))
        else:
            participante = et.SubElement(root, "participante")
            nome = et.SubElement(participante, 'nome')
            nome.text = util.getnome(line)
            nomeinstituicao = util.get_instituicao(line)
            if nomeinstituicao != "":
                instituicao = et.SubElement(participante, 'instituicao')
                instituicao.text = nomeinstituicao
            pap = et.SubElement(participante, 'papel')
            pap.text = papel






f.close()
#prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
#print(formatedXML)

#tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("../xml/EncontrosIniciacaoCientifica.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)

