import sys
from fractions import Fraction

class Sausage:
    def __init__(self, mince = "pork!", volume = 1):
        self.mince = mince
        if Fraction(volume) < 0:
            self.volume = Fraction(0)
        else:
            self.volume = Fraction(volume) * 12

    def __str__(self):
        len_of_sausage = self.volume
        start = ""
        inner = ""
        stop = ""
        while len_of_sausage >= 12:
            len_of_mince = 12 % len(self.mince)
            start += "/" + ("-" * 12) + "\\"
            inner += "|" + (self.mince * (12 // len(self.mince)))
            inner += (self.mince[:len_of_mince]) + "|"
            stop += "\\" + ("-" * 12) + "/"
            len_of_sausage -= 12
        if 0 < len_of_sausage < 12 or self.volume == 0:
            len_of_mince = int(len_of_sausage) % len(self.mince)
            start += "/" + ("-" * int(len_of_sausage)) + "|"
            inner += "|" + (self.mince * (len_of_sausage // len(self.mince)))
            inner += (self.mince[:len_of_mince]) + "|"
            stop += "\\" + ("-" * int(len_of_sausage)) + "|"
        ans = start + "\n" + (inner + "\n") * 3 + stop
        return ans

    def __add__(self, other):
        ans = Sausage(self.mince, (self.volume + other.volume) / 12)
        return ans

    def __sub__(self, other):
        ans = Sausage(self.mince, (self.volume - other.volume) / 12)
        return ans

    def __abs__(self):
        return '{}'.format(self.volume / 12)

    def __mul__(self, other):
        ans = Sausage(self.mince, (self.volume * other) / 12)
        return ans

    def __rmul__(self, other):
        ans = Sausage(self.mince, (self.volume * other) / 12)
        return ans

    def __truediv__(self, other):
        ans = Sausage(self.mince, (self.volume / other) / 12)
        return ans

    def __bool__(self):
        return bool(self.volume)

exec(sys.stdin.read(), globals())
