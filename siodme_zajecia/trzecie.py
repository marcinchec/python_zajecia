#napisz program posiadajacy funkcje ktora oblicza rozklad liczby podanej w argumencie na czynniki pierwsze i zwraca
#wynik w postaci par krotek [(p1,w1),(p2,w2)....] takich ze n=p1^w1*p2^w2...
#rozklad(756)
#[(2,2),(3,3),(7,1)]
from math import *

def rozklad(x):
    if x <= 0:
        return 0
    i = 2
    e = floor(sqrt(x))
    result = []
    while i <= e:
        if x % i == 0:
            result.append(i)
            x /= i
            e = floor(sqrt(x))
        else:
            i += 1
    if x > 1:
        result.append(x)
    tmp=1
    lista_out=[]
    for x in range(1,len(result)):
        if result[x]==result[x-1]:
            tmp+=1
        else:
            lista_out.append((result[x-1],tmp))
            tmp=1
    lista_out.append((result[len(result)-1],tmp))
    return lista_out
#  '2 2 3 3 3 7'
r = rozklad(756)
print r