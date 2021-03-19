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


class Orderedlist:

    def __init__(self):
        self.head = None

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getdata() > item:
                stop = True
            else:
                previous = current
                current = current.getnext()

        newnode = Node(item)
        if previous is None:
            newnode.setnext(self.head)
            self.head = newnode
        else:
            newnode.setnext(current)
            previous.setnext(newnode)

milista = Orderedlist()
milista.add(4)
milista.add(6)
milista.add(5)
