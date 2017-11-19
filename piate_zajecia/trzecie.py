#napisz program ktory wczytuje plik i wyluskuje z niego wszystkie poprawne adresy ipv4
import re

wzorzec = re.compile(r'''^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$''')
def poprawny(adres):
    lista = adres.split('.')
    zm=False
    for x in range(4):
        if int(lista[x])>=0 and int(lista[x])<=255:
            zm=True
        else:
            return False
    return zm

def fun():
    with open("plik1.txt") as f:
        for line in f:
            temp = line.split(' ')
            for x in range(len(temp)):
                for match_object in wzorzec.finditer(temp[x]):
                    if(poprawny(str(match_object.group()))):
                        print match_object.group()

fun()