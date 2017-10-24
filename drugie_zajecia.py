import math
from os import listdir
#drugie zajecia 18.10.2017

# liczby = range(0,20)
# print liczby
# kwadraty = [x**2 for x in liczby]
# print kwadraty

# def f1(a):
#     def f2(b):
#         return a - b
#     return f2
#
# def f3(c):
#     print c(11)
#
# res = f1(5)
# print res(10)
#
# f3(res)


# kwadrat = lambda x: x*x
# print kwadrat(2)

# def generator(n):
#     while n:
#         print 'Generator start %d' %n
#         yield n
#         print 'Generator stop %d' %n
#         n-=1
#
# # for x in generator(5):
# #     print 'Wywolanie %d' %x
#
# gen = generator(5)
# print gen.next()
# print gen.next()

#<-----------------Zadania--------------->
#korzystajac z list skladanych napisz funkcje ktora przyjmuje napis i zwraca liste krotek w postac(slowo, dlugosc slowa)

# def fun(napis):
#     podzial=napis.split()
#     wyjscie = [(x,len(x)) for x in podzial]
#     print wyjscie
#
# fun("to jest jakis napis")

#korzystajac z list skladanych napisz funkcje ktora stworzy liste n elementow ciagu fibonacciego. n jest podawana w konsoli

# n=input("podaj liczbe n\n")
#
# def fib(n):
#     lista=[0,1]
#     [lista.append(lista[x-1]+lista[x-2]) for x in range(2,n)]
#     print lista
#
# fib(n)

#generator liczb ciagu fibonacciego

# def generator():
#     p=0
#     n=1
#     yield p
#     yield n
#     while True:
#         t=p+n
#         p=n
#         n=t
#         yield n
#
# f= generator()
# print f.next()
# print f.next()
# print f.next()
# print f.next()
# print f.next()
# print f.next()
# print f.next()
# print f.next()
# print f.next()
# print f.next()

#zaimplementuj funkcje ktora w argumencie otrzymuje funkcje logiczna oraz liste i zwraca liste elementow spelniajacych warunek podany w przekazywanej funkcji
# l=[1,2,3,4,5,11,23,543,345435]
# def fun(logiczna, n):
#     lista=[x for x in range(0,n+1) if logiczna(x)]
#     print lista
# def logiczna(a):
#     return a%2
# fun(logiczna,10)

#zaimplementuj funkcje ktora przyjmuje liste punktow na plaszczyznie w postaci krotek oraz punkt kontrolny
#funkcja ma zwrocic liste krotek w postaci (odleglosc, punkt(x,y) w kolejnosci od najblizszego do najdalszego pomiedzy
#elementami z listy a punktem kontrolnym
# lista=[(1,0),(2,1),(3,5),(10,20)]
# punkt=(2,10)
# def odleglosc(punkt1, punkt2):
#     return math.sqrt(math.pow(punkt1[0]-punkt2[0],2) + math.pow(punkt1[1]-punkt2[1],2))
# def fun(list,point):
#     return sorted([(odleglosc(x,point),x) for x in list])
# print fun(lista,punkt)
#print odleglosc((2,1),(3,5))

#napisz generator ktory bedzie zwracal nazwy kolejnych plikow z katalogu o podanym rozszerzeniu
#rozszerzenie oraz sciezke podaje uzytkownik w konsoli
#os.listdir(path)
# sciezka=raw_input("Podaj sciezke")
# roz=raw_input("podaj rozszerzenie")
def generator():
    lista=listdir("D:\Virtual Box")
    rozszerzenie=".dll"
    n=len(lista)-1
    while n:
        if lista[n].__contains__(rozszerzenie):
            yield lista[n]
        n-=1

f=generator()
print f.next()
print f.next()
print f.next()
