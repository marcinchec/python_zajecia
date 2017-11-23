#napisz funkcje, ktora pobierze od uzytkownika liczbe i wyswietli jej pierwiastek.
#obsluz wszystkie wyjatki ktore moga wystapic w wyniku dzialania programu
import math


def fun():
    try:
        data = input()
        data=math.sqrt(data)
    except Exception as w:
        print w
    else:
        print data
fun()