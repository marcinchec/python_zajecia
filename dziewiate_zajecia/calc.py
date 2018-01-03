import logging
from Tkinter import *

def dodaj():
    logging.info("Dodawanie "+str(pole.get()))
    pole_val.insert(END,pole.get())
    print pole_val.get()
    pole_action.insert(END,"+")
    pole.delete(0,END)

def odejmij():
    pole_val.insert(END, pole.get())
    #print pole_val.get()
    pole_action.insert(END, "-")
    pole.delete(0, END)

def pomnoz():
    pole_val.insert(END, pole.get())
    #print pole_val.get()
    pole_action.insert(END, "*")
    pole.delete(0, END)

def podziel():
    pole_val.insert(END, pole.get())
    #print pole_val.get()
    pole_action.insert(END, "/")
    pole.delete(0, END)

def wynik():
    try:
        logging.info("Wynik")
        logging.debug("Debugowanie")
        val1 = int(pole_val.get())
        val2 = int(pole.get())
        if(pole_action.get().__eq__("+")):
            pole.delete(0,END)
            res=val1+val2
            pole.insert(END,str(res))
        elif (pole_action.get().__eq__("-")):
            pole.delete(0, END)
            res = val1 - val2
            pole.insert(END, str(res))
        elif (pole_action.get().__eq__("*")):
            pole.delete(0, END)
            res = val1 * val2
            pole.insert(END, str(res))
        elif (pole_action.get().__eq__("/")):
            pole.delete(0, END)
            res = val1 / float(val2)
            pole.insert(END, str(res))
    except Exception as e:
        pole.delete(0, END)
        pole.insert(END, "smth went wrong :( ")
        print "po kazdym obliczeniu dzialania nalezy wcisnac clear"
def clear():
    pole.delete(0,END)
    pole_val.delete(0,END)
    pole_action.delete(0,END)
def zero():
    pole.insert(END,"0")
def jeden():
    pole.insert(END, "1")
def dwa():
    pole.insert(END, "2")
def trzy():
    pole.insert(END, "3")
def cztery():
    pole.insert(END, "4")
def piec():
    pole.insert(END, "5")
def szesc():
    pole.insert(END, "6")
def siedem():
    pole.insert(END, "7")
def osiem():
    pole.insert(END, "8")
def dziewiec():
    pole.insert(END, "8")

root = Tk()
#logging.basicConfig(filename='app.log',level=logging.INFO)
logging.basicConfig(filename='app.log',level=logging.DEBUG)
logging.info("Start")
root.geometry('{}x{}'.format(300,350))
root.resizable(0,0)

pole=Entry(root,justify=RIGHT)
pole.grid(row=0)

pole_val=Entry()
pole_action=Entry()

dodaj=Button(root,text="+",height=3,width=4,command=dodaj)
dodaj.grid(row=1,column=0,sticky=W)

usun=Button(root,text="clear",height=3,width=4,command=clear)
usun.grid(row=1,column=0)

odejmij=Button(root,text="-",width=4,height=3,command=odejmij)
odejmij.grid(row=1,column=0,sticky=E)

pomnoz=Button(root,text="*",width=4,height=3,command=pomnoz)
pomnoz.grid(row=2,column=0,sticky=W)

podziel=Button(root,text="/",width=4,height=3,command=podziel)
podziel.grid(row=2,column=0,sticky=E)

wynik=Button(root,text="=",width=4,height=3,command=wynik)
wynik.grid(row=2,column=0)

val=IntVar()

zero=Button(root,text="0",command=zero,height=2)
zero.grid(row=1,column=1)

jeden=Button(root,text="1",command=jeden,height=2)
jeden.grid(row=1,column=2)

dwa=Button(root,text="2",command=dwa,height=2)
dwa.grid(row=1,column=3)

trzy=Button(root,text="3",command=trzy,height=2)
trzy.grid(row=2,column=1)

cztery=Button(root,text="4",command=cztery,height=2)
cztery.grid(row=2,column=2)

piec=Button(root,text="5",command=piec,height=2)
piec.grid(row=2,column=3)

szesc=Button(root,text="6",command=szesc,height=2)
szesc.grid(row=3,column=1)

siedem=Button(root,text="7",command=siedem,height=2)
siedem.grid(row=3,column=2)

osiem=Button(root,text="8",command=osiem,height=2)
osiem.grid(row=3,column=3)

dziewiec=Button(root,text="9",command=dziewiec,height=2)
dziewiec.grid(row=4,column=1)

root.mainloop()
logging.info("Koniec")