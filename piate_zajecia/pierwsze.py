#napisz funkcje ktora wczytuje plik oraz wczytuje zmienna width w konsoli, nastepnie wyswietla tekst,
#tak ze w jednej linii bedzie nie wiecej niz width znakow

def fun():
    width = input()
    napis=''
    with open("plik1.txt") as f:
        for line in f:
            napis+=line.strip()+' '
    while napis:
        print napis[:width]
        napis=napis[width:]
fun()