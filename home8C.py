import sys

class Dots:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __getitem__(self, item):
        if str(item).isdigit() is True:                            #d[n]    item = n
            step = (self.b - self.a) / (item - 1)
            return (float(self.a + step * i) for i in range(item))
        else:
            if item.step is None:                                  #d[i:n]
                step = (self.b - self.a) / (item.stop - 1)
                return float(self.a + step * item.start)
            else:                                                  #d[i:j:n]
                step = (self.b - self.a) / (item.step - 1)
                start = item.start
                stop = item.stop
                if start is None:
                    start = 0
                if stop is None:
                    stop = item.step
                return (float(self.a + step * i) for i in range(start, stop))


exec(sys.stdin.read(), globals())
