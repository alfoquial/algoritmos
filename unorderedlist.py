class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getdata(self):
        return self.data

    def getnext(self):
        return self.next

    def setnext(self, initnext):
        self.next = initnext

    def setdata(self, newdata):
        self.data = newdata


class Unorderedlist:

    def __init__(self):
        self.head = None

    def add(self, item):
        newnodo = Node(item)
        newnodo.setnext(self.head)
        self.head = newnodo

    def isempty(self):
        return self.head is None

    def search(self, item):
        found = False
        current = self.head
        while current is not None and not found:
            if current.getdata() == item:
                found = True
            else:
                current = current.getnext()
        return found

    def remove(self, item):
        found = False
        current = self.head
        previous = None
        while not found:
            if current.getdata() == item:
                found = True
            else:
                previous = current
                current = current.getnext()

        if previous is None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())

    def size(self):
        cont = 0
        current = self.head
        while current is not None:
            cont = cont + 1
            current = current.getnext()
        return cont

    def append(self, item):
        current = self.head
        newnodo = Node(item)
        while current.getnext() is not None:
            current = current.getnext()

        current.setnext(newnodo)

    def index(self, item):
        current = self.head
        position = 0
        try:
            while current.getdata() != item:
                current = current.getnext()
                position = position + 1
            return position
        except:
            print('{} not found'.format(item))

    def pop(self):
        current = self.head
        previous = None
        while current.getnext() is not None:
            previous = current
            current = current.getnext()
        previous.setnext(None)

    def insert(self, item, pos):
        current = self.head
        previous = None
        newnodo = Node(item)

        for posinsert in range(pos):
            previous = current
            current = current.getnext()

        newnodo.setnext(current)
        previous.setnext(newnodo)

    def pop(self, pos):
        current = self.head
        previous = None

        for posinsert in range(pos):
            previous = current
            current = current.getnext()

        value = current.getdata()
        current = current.getnext()
        previous.setnext(current)

        return value


lista = Unorderedlist()
lista.add(4)
lista.add('libro')
lista.add(23)
lista.add('casa')
lista.insert(5, 2)
