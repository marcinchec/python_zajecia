# zajecia 25.10.2017

import math


# class klasa:
#     zmienna=0
#     def funkcja(self):
#         print 'metoda'
#         self.zmienna=5
# obiekt = klasa()
# obiekt.funkcja()

# class klasa1:
#     def funkcja(self,zmienna):
#         print "wywolanie metody %s. "%zmienna
#         self.funkcja1()
#     def funkcja1(self):
#         print "funkcja2"
#
# obiekt = klasa1()
# obiekt.funkcja("funkcja")

# class klasa:
#     atr1 = None
#     __atr2 = None
#     def setAtr2(self,zmienna):
#         self.__atr2 = zmienna
#     def setAtr3(self,zmienna):
#         self.atr3 = zmienna
#     def add(self):
#         return self.atr1 + self.__atr2 + self.atr3
# obiekt = klasa()
# obiekt.atr1=4
# obiekt.setAtr2(5)
# obiekt.setAtr3(10)
# obiekt._klasa__atr2 = 8
# print obiekt.add()

# class samochod:
#     kolor =None
#     def setKolor(self,kolor):
#         self.kolor=kolor
# class osobowy(samochod):
#     marka="mercedes"
#
# sam = osobowy()
# sam.setKolor('czerwony')
# print ('To jest %s %s')%(sam.kolor, sam.marka)

# class A(object):
#     def funkcja(self):
#         print 'wywolanie A'
# class B(A):
#     def funkcja(self):
#         print "wywolanie B"
#         super(B,self).funkcja()
#
# B().funkcja()

# class A:
#     def __init__(self,zmienna):
#         self.zmienna = zmienna
#     def __add__(self, other):
#         return self.zmienna + other.zmienna
#
# a = A(5)
# b=A(8)
# print a +b

# <--------------------------------Zadania---------------------------------------------->
# zaimplementuj klase "liczba zespolona". klasa ma miec mozliwosc dodawania, odejmowania, mnozenia, dzielenia
# oraz przypisywania z wykorzystaniem standardowych operatorow. Dodatkowo ma posiadac funkcje "modul"
# obliczajaca modul liczby zespolonej oraz mozliwosc porownywania go rowniez przy pomocy standardowych operatorow
# logicznych. Po przekazaniu obiektu do funkcji print ma ona zostac wyswietlona na ekranie

# class liczba_zespolona(object):
#     def __init__(self,im,re):
#         self.im =im
#         self.re=re
#     def __add__(self, other):
#         return liczba_zespolona((self.im + other.im),(self.re+other.re))
#     def __sub__(self, other):
#         return liczba_zespolona((self.im - other.im),(self.re-other.re))
#     def __mul__(self, other):
#         return liczba_zespolona(self.im*(other.im+other.re),self.re*(other.im+other.re))
#     def __div__(self, other):
#         return
#
#     def modul(self,im,re):
#         z=math.sqrt(pow(im,2)+pow(re,2))
#         return abs(z)
#
# l1=liczba_zespolona(7,3)
# l2=liczba_zespolona(4,-7)
# dod=l1+l2
# print '(%d %di)' %(dod.im,dod.re)



# zaimplementuj dwie klasy, Punkt2D i rozszerzajaca ja klase Punkt3D. Kazda z klas ma miec mozliwosc obliczania
# odleglosci miedzy dwoma punktami

# class Punkt2D(object):
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def odleglosc(self,pierwszy,drugi):
#         return math.sqrt(math.pow(pierwszy.x-drugi.x,2) + math.pow(pierwszy.y-drugi.y,2))
#
# class Punkt3D(Punkt2D):
#     def __init__(self,x,y,z):
#         super(Punkt3D,self).__init__(x,y)
#         self.z=z
#     def odleglosc(self,pierwszy,drugi):
#         #print math.sqrt(math.pow(pierwszy.x-drugi.x,2) + math.pow(pierwszy.y-drugi.y,2)+math.pow(pierwszy.z-drugi.z,2))
#         return math.sqrt(math.pow(super(Punkt3D,self).odleglosc(pierwszy,drugi),2) + math.pow(pierwszy.z - drugi.z, 2))
# pierwszy=Punkt2D(2,10)
# drugi=Punkt2D(3,10)
# p1=Punkt3D(10,20,3)
# p2=Punkt3D(20,40,3)
# print pierwszy.odleglosc(pierwszy,drugi)
# print p1.odleglosc(p1,p2)


# zaimplementuj klase samochod posiadajaca prywatne pola marka, pojemnoscBaku, predkoscMaksymalna
# zuzyciePaliwa oraz funkcje publiczne konstruktor, jedz(predkosc,odleglosc) wyswietlajaca
# informacje o predkosci(nie wieksza niz maksymalna), czasie podrozy, zuzyciu paliwa oraz ile razy
# trzeba bedzie tankowac. Jezeli samochod jedzie ponizej 30% lub powyzej 80% predkosci maksymalnej
# to zuzycie paliwa wzrasta o 20%. Nastepnie zdefiniuj klase kabriolet dziedziczaca po samochodzie
# posiadaja dodatkowe pole otwartyDach oraz dwie dodatkowe metody zamknijDach oraz otworzdach.
# Jezeli dach jest otwarty to zuzycie paliwa podczas obliczen w funkcji jedz powinno wzrosnac o 15%


class samochod(object):
    __marka = None
    __pojemnoscBaku = None
    __predkoscMaksymalna = None
    __zuzyciePaliwa = None

    def __init__(self, marka, bak, predkosc, paliwo):
        self.__marka = marka
        self.__pojemnoscBaku = bak
        self.__predkoscMaksymalna = predkosc
        self.__zuzyciePaliwa = paliwo

    def jedz(self, predkosc, odleglosc):
        if (predkosc <= self.__predkoscMaksymalna):
            print "predkosc: " + str(predkosc)
        czas = odleglosc / predkosc
        print "czas podrozy: " + str(czas)
        if ((predkosc <= 0.3 * self.__predkoscMaksymalna) or (predkosc >= 0.8 * self.__predkoscMaksymalna)):
            self.__zuzyciePaliwa*= 1.2
        print "zuzycie paliwa: " + str(self.__zuzyciePaliwa)
        ile_razy = (odleglosc*0.1 / self.__zuzyciePaliwa)
        print "ilosc tankowan: " + str('%.1f'%(ile_razy))
    def set_zuzycie(self,a):
        self.__zuzyciePaliwa*=a
        return self.__zuzyciePaliwa
class kabriolet(samochod):
    __otwartyDach =None

    def __init__(self,marka,bak,predkosc,paliwo,dach):
        super(kabriolet,self).__init__(marka,bak,predkosc,paliwo)
        self.__otwartyDach=dach
    def zamknijDach(self):
        self.__otwartyDach=False
        return self.__otwartyDach
    def otworzDach(self):
        self.__otwartyDach=True
        return self.__otwartyDach
    def jedz(self, predkosc, odleglosc):
        if(self.__otwartyDach):
            super(kabriolet,self).set_zuzycie(1.15)
        super(kabriolet,self).jedz(predkosc,odleglosc)

s1 = samochod("mercedes",40,100,6)
s1.jedz(50,120)
s2 = kabriolet("mercedes",40,100,6,True)
s2.jedz(50,120)

