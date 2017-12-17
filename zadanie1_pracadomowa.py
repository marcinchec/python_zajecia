import urllib2
import re
from bs4 import BeautifulSoup
from bs4.element import Comment
import time

def widocznosc_tagu(element):
    if element.parent.name in ['head','title','style','script','[document]']:
        return False
    if isinstance(element,Comment):
        return False
    return True

def getText(html):
    soup=BeautifulSoup(html,'html.parser')
    caly_tekst=soup.findAll(text=True)
    widoczne_teksty=filter(widocznosc_tagu,caly_tekst)
    czysty_tekst= u" ".join("\n"+x.strip() for x in widoczne_teksty)
    return czysty_tekst

def count_text(link,slownik,which):
    wzorzec = re.compile(r'''[a-z]{2,}''')
    html=urllib2.urlopen(link).read()
    txtfromweb= getText(html)
    txtfromweb=txtfromweb.lower()
    txtfromweb=wzorzec.findall(txtfromweb)
    #print txtfromweb
    #print len(txtfromweb)
    lista = [1, which]
    slownik.update({txtfromweb[0]: lista})
    for x in txtfromweb:
        try:
            slownik.get(x)
            tmp=slownik[x]
            copyoflist=list(tmp)
            copyoflist[0]+=1
            if not which in copyoflist:
                copyoflist.append(which)
            slownik[x]=copyoflist
        except Exception:
            #print "new key to dict"
            slownik.update({x:lista})
    return slownik

def wynik(slownik, listasort):
    lista_slow=[]
    for x in range(5):
        for key, value in slownik.items():
            if value[0]==listasort[x][0]:
                lista_slow.append(key.encode("utf-8"))
    return lista_slow

def getlink(slownik,slowo,linki):
    try:
        lista=[]
        slownik.get(slowo)
        tmp=slownik[slowo]
        for x in range(1,len(tmp)):
            lista.append(linki.get(tmp[x]))
        return lista
    except Exception:
        print "Blad podczas wyszukiwania"

allwords={}
start=time.time()
allwords=count_text("http://www.nytimes.com/2009/12/21/us/21storm.html",allwords,"link1")
allwords=count_text("http://www.nytimes.com/2017/12/05/opinion/donald-trump-needs-friends.html?src=me",allwords,"link2")
allwords=count_text("https://www.nytimes.com/2017/12/07/well/eat/should-you-be-worried-about-the-arsenic-in-your-baby-food.html?rref=collection%2Fsectioncollection%2Fhealth&action=click&contentCollection=health&region=rank&module=package&version=highlights&contentPlacement=2&pgtype=sectionfront",allwords,"link3")
allwords=count_text("https://www.nytimes.com/2017/12/06/sports/soccer/champions-league-draw.html?rref=collection%2Fsectioncollection%2Fsoccer&action=click&contentCollection=soccer&region=stream&module=stream_unit&version=latest&contentPlacement=1&pgtype=sectionfront&mtrref=www.nytimes.com&gwh=61B3E0874DCE39865F546A0EA312AE0D&gwt=pay",allwords,"link4")
allwords=count_text("https://www.nytimes.com/2017/12/05/sports/soccer/champions-league-manchester-united.html?rref=collection%2Fsectioncollection%2Fsoccer&action=click&contentCollection=soccer&region=stream&module=stream_unit&version=latest&contentPlacement=2&pgtype=sectionfront&mtrref=www.nytimes.com&gwh=C091ECF0BAAB4093B18C9CBF8CD39D93&gwt=pay",allwords,"link5")
linki={
    "link1":"http://www.nytimes.com/2009/12/21/us/21storm.html",
    "link2":"http://www.nytimes.com/2017/12/05/opinion/donald-trump-needs-friends.html?src=me",
    "link3":"https://www.nytimes.com/2017/12/07/well/eat/should-you-be-worried-about-the-arsenic-in-your-baby-food.html?rref=collection%2Fsectioncollection%2Fhealth&action=click&contentCollection=health&region=rank&module=package&version=highlights&contentPlacement=2&pgtype=sectionfront",
    "link4":"https://www.nytimes.com/2017/12/06/sports/soccer/champions-league-draw.html?rref=collection%2Fsectioncollection%2Fsoccer&action=click&contentCollection=soccer&region=stream&module=stream_unit&version=latest&contentPlacement=1&pgtype=sectionfront&mtrref=www.nytimes.com&gwh=61B3E0874DCE39865F546A0EA312AE0D&gwt=pay",
    "link5":"https://www.nytimes.com/2017/12/05/sports/soccer/champions-league-manchester-united.html?rref=collection%2Fsectioncollection%2Fsoccer&action=click&contentCollection=soccer&region=stream&module=stream_unit&version=latest&contentPlacement=2&pgtype=sectionfront&mtrref=www.nytimes.com&gwh=C091ECF0BAAB4093B18C9CBF8CD39D93&gwt=pay"
}
# for x in allwords:
#       print str(x)+" "+str(allwords[x])

print "wielkosc slownika= " + str(len(allwords))
print str(time.time()-start) +"  seconds"

posortowane= sorted(allwords.values(),reverse=True)

print "najczesciej wystepujace slowa: "+ str(wynik(allwords,posortowane))
print
szukane=raw_input("podaj szukane slowo: ")

try:
    znaleziono= getlink(allwords,szukane,linki)
    for x in znaleziono:
        print x
except Exception:
    print "Brak slowa w slowniku"