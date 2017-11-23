#napisz program ktory pobiera dokument html i zapisuje go na dysku
import urllib2

response = urllib2.urlopen('https://python.org')
html=response.read()
with open("plik1.xml",'w') as f:
    f.write(html)