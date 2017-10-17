# data = input("podaj cos\n")
# data1 = input ("drugi raz\n")
#
#
# def suma(data,data1):
#     print data+data1
#
# suma(data,data1)

# a=20
# b=40
# if(a<b):
#     print "A"
# else:
#     print "B"
#
# for i in range(0,10):
#     print i
#
# li = [2,3,4.4,'s',"asd"]
#
# print li
#
# li[2]=100
#
# print li
#
# krotka = (10,30,'as')

# imie = raw_input("Podaj imie\n")
# nazwisko =raw_input("Podaj nazwisko\n")
# wiek = input("Podaj wiek\n")
#
# if(wiek>=18):
#     print "Czesc %s %s, jestes pelnoletni"%(imie,nazwisko)
# else:
#     print "Czesc %s %s, jestes niepelnoletni" % (imie, nazwisko)

# a=input("pierwsza")
# b=input("druga")
# c=input("trzecia")
#
# if(a>b):
#     if(a>c):
#         print a
#     else:
#         print c
# elif(b>c):
#     print b
# else:
#     print c

# lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# # print lista
# # for x in lista:
# #     print x.lower()+x.upper()
#
# n=input("podaj liczbe")
# for x in range(0,len(lista),n):
#     print lista[x].lower()+lista[x].upper()
# lista=[]
# ile=input("ile liczb?")
#
# for x in range(0,ile):
#     liczba=input()
#     lista.append(liczba)
#
# kierunek=raw_input("kierunek sortowania malejaco/rosnaco")
# zakres1=input("podaj zakres1")
# zakres2=input("podaj zakres2")
#
# if(kierunek=="malejaco"):
#     lista.sort(reverse=True)
#     for x in range(zakres1-1,zakres2):
#         print lista[x]
# elif(kierunek=="rosnaco"):
#     lista.sort()
#     for x in range(zakres1-1, zakres2):
#         print lista[x]
# else:
#     print "zly kierunek"

# def fib(n):
#     if (n<1):
#         return 0
#     if (n<2):
#         return 1
#     return fib(n-1)+fib(n-2)
# print fib(50)

t="to jest tekst"
print t
def cezar(tekst,klucz):
    szyfr=""
    for x in range(len(tekst)):
        if ord(tekst[x]) > 122 - klucz:
            szyfr += chr(ord(tekst[x]) + klucz - 26)
        else:
            szyfr += chr(ord(tekst[x]) + klucz)
    return szyfr

print cezar(t,3)




