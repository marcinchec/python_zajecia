#zmodyfikuj poprzedni program tak aby wyswietlany tekst byl wysrodkowany w obrebie wprowadzonego rozmiaru
def fun():
    width = input()
    napis=''
    with open("plik1.txt") as f:
        for line in f:
            napis+=line.strip()+' '
    while napis:
        print napis[:width].center(width)
        napis=napis[width:]
fun()