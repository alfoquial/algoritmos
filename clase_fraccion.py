from funcionMCD import mcd


class Fraction:

    def __init__(self, val1, val2):
        self.num = val1
        self.den = val2

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, f):
        num = self.num * f.den + f.num * self.den
        den = self.den * f.den
        k = mcd(num, den)

        return Fraction(num // k, den // k)

    def __eq__(self, f):
        if self.num * f.den == f.num * self.den:
            return True
        else:
            return False

if __name__="__main__":
    fr1 = Fraction(2, 6)
    fr2 = Fraction(1, 3)
    print(fr1+fr2)