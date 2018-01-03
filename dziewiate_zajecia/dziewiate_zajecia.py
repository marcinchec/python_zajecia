#zajecia 13.12.2017


# logger = logging.getLogger(__name__)
# logger.info("info")
# logger.info("debug")
#
# def main():
#     logging.basicConfig(filename='app.log',level=logging.INFO)
#     logging.info("Start")
#     dziewiate_zajecia1.funkcja()
#     logging.info("Koniec")
#
# if __name__=="__main__":
#     main()

# def fnk():
#     d='d'
#     print 'd'
#
# a='a'
# pdb.set_trace()
# b='b'
# pdb.set_trace()
# fnk()
# c='c'
# res=a+b+b
# print res


# lista= ['aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa','b','c','d']
# pdb.set_trace()
# print lista

def num2text(n):
    return{
        1:'jeden',
        2:'dwa',
        3:'trzy'
    }.get(n)


#dodaj logowanie do pliku do kalkulatora wykonanego na poprzednich zajeciach
#wykorzystaj rozne poziomy logowania


#rozwiniecie testow

#przy pomocy modulu pytest-cov zbadaj pokrycie kodu testami
