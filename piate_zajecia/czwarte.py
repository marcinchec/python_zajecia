#napisz walidator dla numerow pesel, ktory sprawdza jego poprawnosc oraz wyluskuje z niego date
#urodzenia w postaci dd-miesiac-rrrr i plec

miesiace = {"1":"styczen",
          "2":"luty",
          "3":"marzec",
          "4":"kwiecien",
          "5":"maj",
          "6":"czerwiec",
          "7":"lipiec",
          "8":"sierpien",
          "9":"wrzesien",
          "10":"pazdziernik",
          "11":"listopad",
          "12":"grudzien",
}

def getrok(miesiac):
    if miesiac > 0 and miesiac < 13:
        return "19"
    elif miesiac > 20 and miesiac < 33:
        return "20"
    elif miesiac > 40 and miesiac < 53:
        return "21"
    elif miesiac > 60 and miesiac < 73:
        return "22"
    elif miesiac > 80 and miesiac < 93:
        return "18"
    else:
        return "niepoprawny pesel"

def getmiesiac(rok, miesiac):
    if rok ==19:
        return miesiac
    elif rok == 20:
        return miesiac-20
    elif rok ==21:
        return miesiac-40
    elif rok==22:
        return miesiac-60
    else:
        return miesiac-80

def valid(pesel):
    checker=[1,3,7,9,1,3,7,9,1,3]
    suma=0
    for i in range(10):
        suma+=(checker[i]*int(pesel[i]))%10
    suma=10-(suma%10)
    return suma

def fun(pesel):
    wynik=""
    if len(pesel)!=11:
        wynik = "nieprawidlowa dlugosc"
        return wynik
    else:
        rok=pesel[0:2]
        miesiac=pesel[2:4]
        tmp = getrok(int(miesiac))
        if tmp == "niepoprawny pesel":
            return "niepoprawny pesel"
        tmp1 = getmiesiac(int(tmp),int(miesiac))
        tmp1 = miesiace.get(str(tmp1))
        dzien=pesel[4:6]
        plec = pesel[9:10]
        if int(plec)%2==0:
            p="kobieta"
        else:
            p="mezczyzna"
        if(valid(pesel)== int(pesel[10])):
            wynik+=dzien+"-"+tmp1+"-"+tmp+rok+" plec: "+p
            return wynik
        else:
            return "nieprawidlowy pesel"
print fun("80072909146")