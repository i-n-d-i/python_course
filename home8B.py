import sys

class Triangle:
    tri = False
    def __init__(self, a, b, c):
        a, b, c = float(a), float(b), float(c)
        self.a = a
        self.b = b
        self.c = c
        if a > 0 and b > 0 and c > 0:
            if a < b + c and b < a + c and c < a + b:
                self.tri = True

    def __abs__(self):
        if self.tri is False:
            return 0
        else:
            p = (self.a + self.b + self.c) / 2.0
            S = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
            return S

    def __eq__(self, other):
        if self.tri is False or other.tri is False:
            return False
        list1 = [self.a, self.b, self.c]
        list1.sort()
        list2 = [other.a, other.b, other.c]
        list2.sort()
        if list1 == list2:
            return True
        return False

    def __lt__(self, other):   # <
        return abs(self) < abs(other)

    def __le__(self, other):   # <=
        return abs(self) <= abs(other)

    def __gt__(self, other):   # >
        return abs(self) > abs(other)

    def __ge__(self, other):   # >=
        return abs(self) >= abs(other)

    def __str__(self):
        return f"{self.a}:{self.b}:{self.c}"

    def __bool__(self):
        return self.tri

exec(sys.stdin.read(), globals())
