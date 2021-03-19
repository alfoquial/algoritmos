class LogicGate:

    def __init__(self, etiqueta):
        self.label = etiqueta
        self.output = None

    def getlabel(self):
        return self.label

    def getoutput(self):
        self.output = self.logicoutput()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, etiqueta):
        LogicGate.__init__(self, etiqueta)
        self.PinA = None
        self.PinB = None

    def getpina(self):
        if self.PinA is None:
            return int(input("Enter Pin A input for gate " + self.getlabel() +
                             "-->"))
        else:
            return self.PinA.getfrom().getoutput()

    def getpinb(self):
        if self.PinB is None:
            return int(input("Enter Pin B input for gate " + self.getlabel() +
                             "-->"))
        else:
            return self.PinB.getfrom().getoutput()

    def setnextpin(self, source):
        if self.PinA is None:
            self.PinA = source
        else:
            if self.PinB is None:
                self.PinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):

    def __init__(self, etiqueta):
        LogicGate.__init__(self, etiqueta)
        self.Pin = None

    def getpin(self):
        if self.Pin is None:
            return int(input("Enter Pin input for Gate" + self.getlabel() +
                             "-->"))
        else:
            return self.Pin.getfrom().getoutput()

    def setnextpin(self, source):
        if self.Pin is None:
            self.Pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self, etiqueta):
        BinaryGate.__init__(self, etiqueta)

    def logicoutput(self):
        a = self.getpina()
        b = self.getpinb()

        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, etiqueta):
        BinaryGate.__init__(self, etiqueta)

    def logicoutput(self):
        a = self.getpina()
        b = self.getpinb()

        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):

    def __init__(self, etiqueta):
        UnaryGate.__init__(self, etiqueta)

    def logicoutput(self):
        pin = self.getpin()

        if pin == 1:
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setnextpin(self)

    def getfrom(self):
        return self.fromgate

    def getto(self):
        return self.togate


def main():
    g1 = AndGate("g1")
    g2 = OrGate("g2")
    c1 = Connector(g1, g2)
    print(g2.getoutput())


if __name__=="__main__":
    main()
