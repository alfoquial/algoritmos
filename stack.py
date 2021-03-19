class Stack:

    def __init__(self):
        self.objetos = []

    def push(self, item):
        self.objetos.append(item)

    def pop(self):
        return self.objetos.pop()

    def peek(self):
        if len(self.objetos) > 0:
            return self.objetos[len(self.objetos) - 1]
        return False

    def isempty(self):
        return self.objetos == []

    def size(self):
        return len(self.objetos)

    def __str__(self):
        return str(self.objetos)

    def reverse(self):
        return self.objetos.reverse()






def parentesis(cadena):
    pila = Stack()
    for caracter in cadena:
        if caracter == '(':
            pila.push(caracter)
        else:
            if pila.peek() == '(':
                pila.pop()
            else:
                balance = False
                return balance
    return pila.size() == 0


def balanced(cadena):
    pila = Stack()
    for simbolo in cadena:
        if simbolo in "([{":
            pila.push(simbolo)
        else:
            if (simbolo == ')' and pila.peek() == '(') or (simbolo == ']' and
            pila.peek() == '[') or (simbolo == '}' and pila.peek() == '{'):
                pila.pop()
            else:
                balance = False
                return balance
    return pila.size() == 0
