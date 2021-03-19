class Invertir:
    def __init__(self, cadena):
        self.cadena = cadena
        self.puntero = len(cadena)

    def __iter__(self):
        return self

    def __next__(self):
        if self.puntero == 0:
            raise StopIteration
        self.puntero = self.puntero - 1
        return self.cadena[self.puntero]


cadena_invertida = Invertir("una cadena para invertir")

iter(cadena_invertida)


for caracter in cadena_invertida:
    print(caracter, ' ')
