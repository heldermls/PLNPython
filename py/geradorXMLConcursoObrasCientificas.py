#from xml.etree.ElementTree import Element,ElementTree
import re
import io
from py import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('ConcursosObrasCientificas')
tree = et.ElementTree(root)
nome = ""
ano = ""
with open('../txt/ConcursosObrasCientificas.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
    lines = clean_text.splitlines()
# gerando iterador para ter acesso ao next()
itr = iter(lines)
for line in itr:

    if not line or bool(re.match(r'\s\s*', line)):
        print("linha vazia")
    else:

        searchtipoconcurso = re.search(r'#', line)
        ehconcurso = bool(searchtipoconcurso)
        if searchtipoconcurso:
            txttipoobra = line.replace("#", "")
        searchnome = re.search(r'(.*),\s*(\d\d\d\d)', line)
        ehnome = bool(searchnome)
        if ehconcurso:
            tipoconcurso = searchtipoconcurso.group(0)
            tipoconcurso = tipoconcurso.replace("#", "")
        elif ehnome:
            nome = searchnome.group(1)
            ano = searchnome.group(2)
            participante = et.SubElement(root, "vencedor")
            nomepart = et.SubElement(participante, 'nome')
            nomepart.text = nome
            obra = et.SubElement(participante, 'obra')

            anoobra = et.SubElement(obra, 'ano')
            anoobra.text = ano
            tipoobra = et.SubElement(obra, 'categoria')
            tipoobra.text = txttipoobra
        else:
            nomeobra = line.strip()
            nmobra = et.SubElement(obra, 'titulo')
            nmobra.text = nomeobra


f.close()
# prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
# print(formatedXML)

# tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("../xml/ConcursosObrasCientificas.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)

