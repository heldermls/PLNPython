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
        linesmatch = "{match}".format(matchNum=matchNum, start=match.start(), end=match.end(), match=match.group())
        linesmatch = linesmatch.splitlines()
        subcursos = linesmatch.copy()
        subcursos.remove(macrocurso)
        lines.remove(macrocurso)
        curso = et.SubElement(root, "curso")
        nome = et.SubElement(curso, 'nome')
        nome.text = util.getnome(macrocurso)
        nomesubcurso, nomeprofessor, ano = "", "", ""
        for linha in subcursos:
            lines.remove(linha)
            res = re.search(r'\d\d\d\d', linha)
            if(bool(res)):
                ano = res.group(0)
                nomeprofessor = util.getnome(linha).replace(",", '')
                nomeprofessor = nomeprofessor.replace(ano, "").strip()
                continue
            else:
                nomesubcurso = linha.strip()
                subcurso = et.SubElement(curso, "subcurso")
                titulosubcurso = et.SubElement(subcurso,"nomesubcurso")
                titulosubcurso.text = nomesubcurso
                professor = et.SubElement(subcurso, "professor")
                professor.text = nomeprofessor
                anosubcurso = et.SubElement(subcurso, "ano")
                anosubcurso.text = ano

    formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
    #print(formatedXML)

    #print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
    #                                                                    end=match.end(), match=match.group()))



    for line in lines:

        if not line or bool(re.match(r'\s\s*', line)):
             print("linha vazia")
        else:

            res = re.search(r'\d\d\d\d', line)
            if (not bool(res)):
                nomecurso = line.strip()
                #print(nomecurso)
                curso = et.SubElement(root, "curso")
                nome = et.SubElement(curso, 'nome')
                nome.text = nomecurso
                continue

            else:
                ano = res.group(0)
                nomeprofessor = util.getnome(line).replace(",", '')
                nomeprofessor = nomeprofessor.replace(ano, "").strip()
                instituicao = util.get_instituicao(line)
                nomeprofessor = nomeprofessor.replace(instituicao, "")
                professor = et.SubElement(curso, "professor")
                nomeprof = et.SubElement(professor, "nome")
                nomeprof.text = nomeprofessor
                instprof = et.SubElement(professor, "instituicao")
                instprof.text = instituicao
                anocurso = et.SubElement(curso, "ano")
                anocurso.text = ano



f.close()
#prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
#print(formatedXML)

#tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("../xml/Cursos.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)


