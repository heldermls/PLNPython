# from xml.etree.ElementTree import Element,ElementTree
import re
import io
import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('comissoes')
tree = et.ElementTree(root)
with open('Comites.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
    lines = clean_text.splitlines()
#gerando iterador para ter acesso ao next()

for line in lines:
    # if its a break of subelements  - that is an empty space

    if not line:
        # add the next subelement and get it as celldata
        # bienio = ET.SubElement(root, 'bienios')
        print("linha vazia")
    else:

        ehbienio = bool(re.search('Bi.*nio', line))
        search = re.search('Comit.*|Comiss.*|Pr.mio.*|Conse.*', line)
        ehcomite = bool(search)
        ehnome = (not ehcomite) and (not ehbienio)
        if ehbienio:
            anos = util.getbienios(line)

            ano_inicio = anos[0]

            ano_fim = anos[1]
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
            nomecomite.text = cmt
            anoI = et.SubElement(comite, 'ano')
            anoI.text = anos[0]
            anoF = et.SubElement(comite, 'ano')
            anoF.text = anos[1]


f.close()
#prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
#print(formatedXML)

#tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("ComissoesFormatado.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)


