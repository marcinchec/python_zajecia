#1. przygotuj okno skladajace sie z jednego buttonu u trzech radiobuttonow okreslajacych podstawowe kolory
#zaznaczenie radio buttonow zmienia kolor tekstu dla przycisku, wcisniecie przycisku powoduje wyswietlenie teksty
from Tkinter import *

def fun():
    print 'Wcisniety'

def test():
    if v.get()==1:
        przycisk.config(fg='red')
    elif v.get()==2:
        przycisk.config(fg='blue')
    else:
        przycisk.config(fg='green')

root = Tk()

root.geometry('{}x{}'.format(200,100))

v=IntVar()

przycisk=Button(root,text="TEXT",command=fun)
przycisk.pack()

Radiobutton(root,text="Red",variable=v,value=1,command=test).pack(anchor=W)
Radiobutton(root,text="Blue",variable=v,value=2,command=test).pack(anchor=W)
Radiobutton(root,text="Green",variable=v,value=3,command=test).pack(anchor=W)

root.mainloop()