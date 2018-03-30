# from xml.etree.ElementTree import Element,ElementTree
import re
import io
import unicodedata
import xml.dom.minidom as minidom
import xml.etree.ElementTree as et

root = et.Element('encontros')
tree = et.ElementTree(root)
with open('../txt/Encontros.txt', encoding="utf8") as f:
    txt = f.read()
    clean_text = unicodedata.normalize("NFKD", txt)
    lines = clean_text.splitlines()


for line in lines:

    if not line or bool(re.match(r'\s\s*', line)):
        print("linha vazia")
    else:
        diafim = None
        res = line.split(",")
        estado = res[-1].strip()
        cidade = res[1].strip()
        strdatas = res[0]
        dias = re.findall(r'\s\d\d\s',strdatas)
        diainicio = dias[0].strip()
        n = len(dias)
        if n > 1:
            diafim = dias[1]
        resmes = re.search(r'setembro|outubro', strdatas)
        mes = resmes[0].strip()
        if mes == "setembro":
            mesdata = 9
        if mes == "outubro":
            mesdata = 10
        resano = re.search(r'\d\d\d\d', strdatas)
        ano = resano[0]
        encontro = et.SubElement(root, "encontro")



        cid = et.SubElement(encontro, 'cidade')
        cid.text = cidade

        est = et.SubElement(encontro, "estado")
        est.text = estado

        dataini = et.SubElement(encontro, "datainicio")
        dataini.text = diainicio.strip() + '-' + mes + '-' + ano

        if diafim is not None:
            datafim = et.SubElement(encontro, "datafim")
            datafim.text = diafim.strip() + "-" + str(mesdata) + "-" + ano

f.close()
#prettify xml

formatedXML = minidom.parseString(et.tostring(root)).toprettyxml(indent=" ").strip()
#print(formatedXML)

#tree.write('diretorias.xml',  method='xml')
# write the formatedXML to file.
with io.open("../xml/Encontros.xml", "w+", encoding="utf-8") as f:
    f.write(formatedXML)


