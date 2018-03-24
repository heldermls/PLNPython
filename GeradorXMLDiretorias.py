# from xml.etree.ElementTree import Element,ElementTree
import re
import io
import util_diretorias as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('root')
tree = et.ElementTree(root)
with open('diretorias_teste.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
    lines = clean_text.splitlines()
#gerando iterador para ter acesso ao next()
itr = iter(lines)
for line in itr:
    # if its a break of subelements  - that is an empty space

    if not line:
        # add the next subelement and get it as celldata
        # bienio = ET.SubElement(root, 'bienios')
        print("linha vazia")
    else:

        ehbienio = bool(re.search('Bi.*nio', line))
        search = re.search('Presidente:|Secret.*ri. Executiv.*:|Secret.*ri. Adjunt.*:|Diretoria:', line)
        cargo = ""
        ehcargo = bool(search)
        ehconselho = bool(re.search('Conselho Fiscal', line))

        if ehbienio:
            bienio = et.SubElement(root, 'bienio')
            anos = util.getbienios(line)
            ano_inicio = et.SubElement(bienio, "ano_inicio")
            ano_inicio.text = anos[0]
            ano_fim = et.SubElement(bienio, "ano_fim")
            ano_fim.text = anos[1]
            
        elif ehcargo:
            cargo = search.group(0).replace(":", "")

            cargo = cargo.replace(" ", "")
            res = re.search(r'Adjunt.*', cargo)
            if res != None:
                cargo = "SecretariaAdjunta"
            res = re.search(r'Executiv.*', cargo)
            if res != None:
                cargo = "SecretariaExecutiva"
            res = re.search(r'Diret.*', cargo)
            if res != None:
                cargo = "Diretor"

            cg = et.SubElement(bienio,   cargo + "")
            nome = et.SubElement(cg, 'nome')
            nome.text = util.getnome(line)

            nomeinstituicao = util.get_instituicao(line)
            if nomeinstituicao != "":
                instituicao = et.SubElement(cg, 'instituicao')
                instituicao.text = nomeinstituicao
        elif ehconselho:
            line = next(itr)

            cons = et.SubElement(bienio, 'conselheiro')
            nome = et.SubElement(cons, 'nome')
            nome.text = util.getnome(line)
            string = util.getnome(line)

            nomeinstituicao = util.get_instituicao(line)
            if nomeinstituicao != "":
                instituicao = et.SubElement(cons, 'instituicao')
                instituicao.text = nomeinstituicao

            line = next(itr)
            cons = et.SubElement(bienio, 'conselheiro')
            nome = et.SubElement(cons, 'nome')
            nome.text = util.getnome(line)

            nomeinstituicao = util.get_instituicao(line)
            if nomeinstituicao != "":
                instituicao = et.SubElement(cons, 'instituicao')
                instituicao.text = nomeinstituicao

            line = next(itr)
            cons = et.SubElement(bienio, 'conselheiro')
            nome = et.SubElement(cons, 'nome')
            nome.text = util.getnome(line)
            nomeinstituicao = util.get_instituicao(line)
            if nomeinstituicao != "":
                instituicao = et.SubElement(cons, 'instituicao')
                instituicao.text = nomeinstituicao


f.close()
#prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
print(formatedXML)

tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("DiretoriasFormatado.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)


