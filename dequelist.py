class Cola:

    def __init__(self):
        self.items = []

    def isempty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def hot_potato(vueltas, *child):
    micola = Cola()
    for nombre in child:
        micola.enqueue(nombre)

    while micola.size() > 1:
        for vez in range(vueltas):
            micola.enqueue(micola.dequeue())

        micola.dequeue()

    return micola.dequeue()


ganador = print(hot_potato(1, 'pepe', 'juan', 'pedro'))
