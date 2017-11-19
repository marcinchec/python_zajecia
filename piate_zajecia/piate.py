#napisz program, ktory magazynuje informacje o posiadanych ksiazkach(tytul, numer isbn, autor(
#program ma miec mozliwosc dodawania, usuwania, wyswietlania pozycji oraz zapisu stanu
#programu do pliku jak i mozliwosc jego wczytania. sciezke do pliku podajemy w parametrze uruchomieniowym skryptu
import pickle

class Ksiazka(object):
    tytul=None
    isbn=None
    autor=None
    def __init__(self,tytul, isbn, autor):
        self.tytul=tytul
        self.isbn=isbn
        self.autor=autor
    def __eq__(self, other):
        return (self.autor == other.autor and self.isbn == other.isbn and self.tytul == other.tytul)

def dodaj(nowa,lista):
        lista.append(nowa)
        print "Adding book..."
        return lista
def usun(dousuniecia,lista):
        for x in range(len(lista)-1):
            if dousuniecia==lista[x]:
                lista.pop(x)
        print "Removing book..."
        return lista
def pozycja(ksiazka,lista):
        for x in range(len(lista)-1):
            if ksiazka==lista[x]:
                return x
def save(lista,plik):
        pickle.dump(lista, open(plik,"wb"))
        print "Serialize..."
def deserialize(plik):
        lista=pickle.load(open(plik,"rb"))
        print "Deserialize..."
        return lista
lista=[]

ks1=Ksiazka("pierwsza",9999,"aaa bbb")
ks2=Ksiazka("druga",8833,"asddsa dfgdfg")
ks3=Ksiazka("trzecia",4356,"fsdfsd dsfsdf")

lista=dodaj(ks1,lista)
lista=dodaj(ks2,lista)
lista=dodaj(ks3,lista)

save(lista,"test.txt")
lista=usun(ks1,lista)
lista=deserialize("test.txt")

for x in lista:
    print x.tytul
    print x.autor
    print x.isbn