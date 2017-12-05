#napisz klase implementacje wlasnej obiektowej listy. Program powinien posiadac podstawowe operacje, takie jak dodawanie
#usuwanie, sortowanie, posiadac przeciazaone operatory i zglaszac niezbedne wyjatki

class MyNode(object):

    def __init__(self,data):
        self.data = data
        self.nextelement = None
        self.index=None

    def set_next(self, new_next):
        self.nextelement = new_next

    def get_next(self):
        return self.nextelement

    def get_data(self):
        return self.data

    def __str__(self):
        return str(self.data)

class MyList(object):

    def __init__(self):
        self.head = None
        self.size=0

    def addtolist(self, data):
        if self.head == None:
            node = MyNode(data)
            self.head = node
            self.size += 1
            return
        else:
            node=self.head
            while node.nextelement != None:
                node=node.nextelement
            new_node=MyNode(data)
            node.nextelement=new_node
            self.size += 1
            return

    def removefromlist(self,data):
        current=self.head
        previous=None
        found=False
        while current and found is False:
            if current.data == data:
                found=True
            else:
                previous=current
                current=current.get_next()
        if current is None:
            raise Exception("Data doesnt exists in list")
        if previous is None:
            self.head=current.get_next()
        else:
            previous.set_next(current.get_next())

    def printlist(self):
        current=self.head
        while current:
            print str(current),
            current=current.nextelement
        print

    def sizeoflist(self):
        return self.size

ll = MyList()
ll.addtolist(132)
ll.addtolist(20)
ll.addtolist(70)
ll.addtolist(40)

ll.printlist()

ll.removefromlist(20)

ll.printlist()
