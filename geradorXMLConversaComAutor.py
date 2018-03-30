# from xml.etree.ElementTree import Element,ElementTree
import re
import io
import util_strings as util
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('autores')
tree = et.ElementTree(root)
with open('ConversaComAutor.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
    lines = clean_text.splitlines()


for line in lines:
    # if its a break of subelements  - that is an empty space

    if not line or bool(re.match(r'\s\s*', line)):
        
        print("linha vazia")
    else:

        colaborador = et.SubElement(root, "autor")
        nome = et.SubElement(colaborador, 'nome')
        txtnome = line.split(',')[0]
        nome.text = util.getnome(txtnome)

        instituicao = et.SubElement(colaborador, "instituicao")
        instituicao.text = util.get_instituicao(txtnome)

        ano = et.SubElement(colaborador,"ano")
        res = re.search(r"\d\d\d\d", line)
        ano.text = res.group(0)



f.close()
#prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
#print(formatedXML)

#tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("ConversaComAutor.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)


