import re


def sohletras(str):
    result = re.search('\(|\)', str)
    if result != None:

        return False

    else:
        return True

def contem_parenteses(str):
    result = re.search('\(', str)
    if result != None:

        return False

    else:
        return True


def getbienios(line):
    lst = line.split(" ")
    filtrado = lst[1]
    bienios = filtrado.split("-")
    return bienios


def getnome(line):
    res = re.search(r'.*:', line)
    string = ""
    if res != None:
        remove = res.group(0)
        string = line.replace(remove, "")
    else:
        string = line
    res = re.search(r'\(.*\)', string)
    if res != None:
        remove = res.group(0)
        string = string.replace(remove, "")

    return string

def getdiretor(line):
    res = re.search(r'.*:', line)
    string = ""
    if res != None:
        remove = res.group(0)
        string = line.replace(remove, "")
        res = re.search(r'\(.*\)', string)
    if res != None:
        remove = res.group(0)
        string = string.replace(remove, "")

    return string

def get_instituicao(line):
    result = re.search(r'\(.*\)', line)
    instituicao = ""
    if result != None:
        instituicao = result.group(0)
        instituicao = instituicao.replace('(', '')
        instituicao = instituicao.replace(')', '')
    return instituicao
