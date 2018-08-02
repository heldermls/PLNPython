# from xml.etree.ElementTree import Element,ElementTree
import re
import io
from py import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('diretorias')
tree = et.ElementTree(root)
anos = [0, 0]
with open('../txt/Diretorias.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
    lines = clean_text.splitlines()
#gerando iterador para ter acesso ao next()
itr = iter(lines)
for line in itr:

    if not line or bool(re.match(r'\s\s*', line)):
        print("linha vazia")
    else:

        ehbienio = bool(re.search('Bi.*nio', line))
        searchcargo = re.search('Presidente:|Secret.*ri. Executiv.*:|Secret.*ri. Adjunt.*:|Diretoria:', line)
        ehcargo = bool(searchcargo)
        ehconselho = bool(re.search('Conselho Fiscal', line))

        ehnome = (not ehcargo) and (not ehbienio) and (not ehconselho)
        cgo = ""
        cargo = None


        if ehbienio:
            anos = util.getbienios(line)
            ano_inicio = anos[0]
            ano_fim = anos[1]


        if ehcargo or ehnome:

            if ehnome:
                cgo = "Conselheiro"
            else:
                cgo = line.split(':')[0]
                cgo = cgo.replace(":", "")
                cgo = cgo.replace(" ", "")
                res = re.search(r'Adjunt.*', cgo)
                if res != None:
                    cgo = "SecretariaAdjunta"
                res = re.search(r'Executiv.*', cgo)
                if res != None:
                    cgo = "SecretariaExecutiva"
                res = re.search(r'Diret.*', cgo)
                if res != None:
                    cgo = "Diretor"
            participante = et.SubElement(root, "participante")
            nome = et.SubElement(participante, 'nome')
            nome.text = util.getnome(line)
            nomeinstituicao = util.get_instituicao(line)
            if nomeinstituicao != "":
                instituicao = et.SubElement(participante, 'instituicao')
                instituicao.text = nomeinstituicao
            cargo = et.SubElement(participante, 'cargo')
            #nomecargo = et.SubElement(cargo, 'nomecargo')
            cargo.text = cgo

            anoI = et.SubElement(participante, 'anoI')
            anoI.text = anos[0]
            anoF = et.SubElement(participante, 'anoF')
            anoF.text = anos[1]






f.close()
#prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
#print(formatedXML)

#tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("../xml/DiretoriasModificado.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)

