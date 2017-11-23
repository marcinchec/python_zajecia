# Napisz klase, ktora bedzie przechowywac adresy e-mail. Konstruktor ma przyjmowac napis,
# bedacy adresem. Jesli zostanie podany niewlasciwy adres, konstruktor ma zglaszac wyjatek
# odpowiedniej klasy.
import re

class AdresyException(Exception):
    pass
class Adresy(object):
    adresy=None
    def __init__(self,adres):
        regex_email = re.compile(
            r'''(?P<adres>
              (?P<login>[\w+.]+)      # login, np. m.j.panczyk+umcs.pl
              @                       # znak @
              (?P<domena>\w+(\.\w+)+) # domena, np. gmail.com
            )''',
            re.IGNORECASE | re.VERBOSE
        )

        if not regex_email.match(adres):
            raise AdresyException("wyjatek zlego adresu e-mail")
        else:
            self.adresy=adres

try:
    b=Adresy("asdfwp.pl")
except Exception as a:
    print a
else:
    print b.adresy
