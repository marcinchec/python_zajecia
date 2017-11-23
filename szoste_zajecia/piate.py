#Napisz prosty czytnik RSS, Program ma miec mozliwosc zapamietywania ulubionych kanalow
#wiadomosci powinny byc czytelnie sformatowane
from xml.dom import minidom
import urllib2

response = urllib2.urlopen('https://www.blog.pythonlibrary.org/feed/')
html=response.read()
with open("plik1.xml",'w') as f:
    f.write(html)

doc=minidom.parse("plik1.xml")
els=doc.getElementsByTagName("channel")
for el in els:
    itemy=el.getElementsByTagName("item")
    for el1 in itemy:
        category = el1.getElementsByTagName("category")
        for x in range(len(category)):
            wynik= category[x].firstChild.data
            print ("%s") %(wynik)
