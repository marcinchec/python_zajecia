#2. napisz prosty sekundnik odliczajacy czas do zadanego momentu
#odliczanie rozpoczyna sie po wcisnieciu przycisku start. Kiedy czas sie skonczy odliczanie zatrzymuje sie a program
#wyswietla komunikat o zakonczeniu odliczania
from Tkinter import *
import time

import math


def startcount():
    if not pole.get().upper().isupper():
        czas=int(pole.get())
        start=time.time()
        elapsed=0
        while elapsed+1 < czas:
            elapsed=time.time()-start
            time.sleep(1)
            #print math.floor(elapsed)
        print "odliczanie zakonczylo sie"
root=Tk()
root.geometry('{}x{}'.format(200,100))

pole=Entry(root)
pole.pack()
pole.insert(0,0)

przycisk=Button(root,text="START",command=startcount)
przycisk.pack()

root.mainloop()