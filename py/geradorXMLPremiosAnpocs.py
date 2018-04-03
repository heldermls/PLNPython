# from xml.etree.ElementTree import Element,ElementTree
import re
import io
from py import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('PremiosANPOCS')
tree = et.ElementTree(root)
anos = [0, 0]
with open('../txt/PremiosAnpocs.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
    lines = clean_text.splitlines()
#gerando iterador para ter acesso ao next()
itr = iter(lines)
for line in itr:

    if not line or bool(re.match(r'\s\s*', line)):
        print("linha vazia")
    else:

        searchpremio = re.search(r'Pr.*mio', line)
        ehpremio = bool(searchpremio)

        if ehpremio:
            txtpremio = line.strip()


        else:
            res = re.findall(r"\d\d\d\d", line)
            ano = res[0]
            linha = line.split(",")[0]
            instituicao = util.get_instituicao(linha)
            nomepremiado = util.getnome(linha)
            premiado = et.SubElement(root, "premiado")
            nome = et.SubElement(premiado, 'nome')
            nome.text = nomepremiado
            inst = et.SubElement(premiado, "instituicao")
            inst.text = instituicao.strip()
            premio = et.SubElement(premiado, "premio")
            nomepremio = et.SubElement(premio, "nomepremio")
            nomepremio.text = txtpremio
            anopremio = et.SubElement(premio, "ano")
            anopremio.text = ano



f.close()
#prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
#print(formatedXML)

#tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("../xml/PremiosAnpocs.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)

