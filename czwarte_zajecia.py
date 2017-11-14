#<-----------------Zadania------------------------>
# napisz funckje ktora przyjmuje napis w formacie:
# "'k1:w1
# k2:w2
# k3:w3"'
# i zwraca slownik w postaci : 'k1':'w1', 'k2':'w2','k3':'w3'

# def fun(napis):
#     print napis
#     slownik = {}
#     lista = napis.split('\n')
#     for x in range(len(lista)):
#         tmp=lista[x]
#         next=tmp.split(':')
#         slownik.update({next[0]:next[1]})
#     print slownik
#
# napis ='''k1:w1
# k2:w2
# k3:w3'''
# fun(napis)


#zmodyfikuj poprzedni program tak, aby identycznie zdefiniowany napis byl wczytywany z pliku, nazwa pliku w parametrze
# def fun(file1):
#     slownik = {}
#     with open(file1) as plik:
#         napis=plik.read()
#     print napis
#     napis=napis[3:-3]
#     lista = napis.split('\n')
#     for x in range(len(lista)):
#         tmp=lista[x]
#         next=tmp.split(':')
#         slownik.update({next[0]:next[1]})
#     print slownik
#
# fun("plik.txt")

#napisz program ktory w parametrze przyjmuje nazwe pliku. Program na stworzyc slownik w ktorym zostanie zliczona ilosc
#wystapien danego slowa we wczytanym tekscie

# def fun(plik):
#     with open(plik) as f:
#         napis=f.read()
#     print napis
#     napis=napis.split('\n')
#     #print napis
#     lista=[]
#     slownik={}
#     for x in range(len(napis)):
#         tmp=napis[x].split(' ')
#         for x in range(len(tmp)):
#             lista.append(tmp[x])
#             key=tmp[x]
#             if key in slownik:
#                 slownik[key]+=1
#             else:
#                 slownik[key]=1
#     print lista
#     print slownik
#
# fun("plik.txt")


#napisz program ktory w parametrze otrzymuje nazwe pliku lub znak '-' oraz ciag znakow.
#program ma wczytac pliki i wyswietlic te linie w ktorych znajduje sie podany ciag znakow
#jezeli zamiast nazwy pliku jest znak to linie sa wczytane ze standardowego wejscia
#pusta linia konczy wczytywanie

# def fun(nazwa,ciag):
#     if nazwa=='-':
#         pierwsze=True
#         while(pierwsze or data != ''):
#             pierwsze=False
#             data=raw_input()
#             if data.__contains__(ciag):
#                 print data
#
#     else:
#         with open(nazwa) as f:
#             for line in f:
#                 if line.__contains__(ciag):
#                     print line
#
# fun("-","ala")


#napisz program ktory w parametrze otrzymuje dwie nazwy plikow
#program ma wczyac jeden plik, zaszyfrowac go szyfrem cezara i zapisac pod nowa nazwa z parametru
def szyfruj(txt):
    KLUCZ=5
    zaszyfrowny = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - KLUCZ:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ - 26)
        else:
            zaszyfrowny += chr(ord(txt[i]) + KLUCZ)
    return zaszyfrowny

def fun(plik1,plik2):
    with open(plik1) as f:
        for line in f:
            wynik=szyfruj(line)
            with open(plik2,'a') as f1:
                print wynik
                f1.write(wynik+'\n')


fun("plik.txt","plik1.txt")