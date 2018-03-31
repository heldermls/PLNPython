# from xml.etree.ElementTree import Element,ElementTree
import re
import io
from py import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('cursos')
tree = et.ElementTree(root)
with open('../txt/Cursos.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
    lines = clean_text.splitlines()
regex = r"(Temas.*|Reinv.*)\n(.*\s\(.*\),\s*\d\d\d\d\n.*\n)+"
matches = re.finditer(regex, clean_text, re.UNICODE)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    macrocurso = match.group(1)
    print(macrocurso)
    linesmatch = "{match}".format(matchNum=matchNum, start=match.start(), end=match.end(), match=match.group())
    linesmatch = linesmatch.splitlines()
    subcursos = linesmatch.copy()
    subcursos.remove(macrocurso)

    curso = et.SubElement(root, "curso")
    nome = et.SubElement(curso, 'nome')
    nome.text = util.getnome(macrocurso)

    for linha in subcursos:
        res = re.search(r'\d\d\d\d', linha)
        if(bool(res)):
            ano = res.group(0)

    print(linesmatch)
    print(subcursos)
    #print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
    #                                                                    end=match.end(), match=match.group()))



for line in lines:

    if not line or bool(re.match(r'\s\s*', line)):
        print("linha vazia")
    else:
        x = 0



f.close()
#prettify xml
'''
formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
#print(formatedXML)

#tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("../xml/Colaboradores.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)

'''
