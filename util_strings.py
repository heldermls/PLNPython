import re



def getbienios(line):
    lst = line.split(" ")
    filtrado = lst[1]
    bienios = filtrado.split("-")
    return bienios


def getnome(line):
    res = re.search(r'.*:', line)
    string = ""
    if res is not None:
        remove = res.group(0)
        string = line.replace(remove, "")
    else:
        string = line
    res = re.search(r'\(.*\)', string)
    if res is not None:
        remove = res.group(0)
        string = string.replace(remove, "")

    return string.strip()



def get_instituicao(line):
    result = re.search(r'\(.*\)', line)
    instituicao = ""
    if result is not None:
        instituicao = result.group(0)
        instituicao = instituicao.replace('(', '')
        instituicao = instituicao.replace(')', '')
    return instituicao

def periodoporextenso(anoinicio,anofim):
    ai = int(anoinicio)
    af = int(anofim)
    retorno = anoinicio
    if ai > af:
        temp = af
        af = ai
        ai = temp
    ano = ai+1
    while ano < af + 1:
        retorno = retorno + ", " + str(ano)
        ano = ano + 1
    return retorno.strip()

def explodeperiodo(line):
    res = re.findall(r'\d\d\d\d-\d\d\d\d', line)

    tamanho = len(res)
    i = 0
    retorno = line

    while i < tamanho:
        st = res[i].split('-')
        retorno = retorno.replace(res[i], periodoporextenso(st[0], st[1]))
        i = i + 1

    return retorno

