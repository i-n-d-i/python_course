class DivStr(str):
    def __getitem__(self, item):
        return DivStr(str(self).__getitem__(item))
    def __add__(self, other):
        return DivStr(str(self).__add__(other))
    def __mul__(self, other):
        return DivStr(str(self).__mul__(other))
    def __rmul__(self, other):
        return DivStr(str(self).__rmul__(other))

    def lower(self):
        return DivStr(str(self).lower())
    def upper(self):
        return DivStr(str(self).upper())

    def removeprefix(self, prefix):
        return DivStr(str(self).removeprefix(prefix))
    def removesuffix(self, suffix):
        return DivStr(str(self).removesuffix(suffix))

    def strip(self, chars = None):
        return DivStr(str(self).strip(chars))
    def rstrip(self, chars = None):
        return DivStr(str(self).rstrip(chars))
    def lstrip(self, chars = None):
        return DivStr(str(self).lstrip(chars))

    def ljust(self, width, fillchar = ' '):
        return DivStr(str(self).ljust(width, fillchar))
    def rjust(self, width, fillchar = ' '):
        return DivStr(str(self).rjust(width,fillchar))
    def center(self, width, fillchar = ' '):
        return DivStr(str(self).center(width,fillchar))

    def capitalize(self):
        return DivStr(str(self).capitalize())
    def casefold(self):
        return DivStr(str(self).casefold())
    def expandtabs(self, tabsize = 8):
        return DivStr(str(self).expandtabs(tabsize))
    def join(self, iter):
        return DivStr(str(self).join(iter))
    def replace(self, old, new, count = -1):
        return DivStr(str(self).replace(old,new, count))
    def swapcase(self):
        return DivStr(str(self).swapcase())
    def title(self):
        return DivStr(str(self).title())
    def translate(self, table):
        return DivStr(str(self).translate(table))
    def zfill(self, width):
        return DivStr(str(self).zfill(width))

    def __floordiv__(self, other):
        lst = []
        if len(self) < other:
            return [''] * other
        num = len(self) // other
        i = 0
        while other:
            lst.append(self[i:i+num])
            i += num
            other -= 1
        return lst

    def __mod__(self, other):
        mod = len(self) % other
        return DivStr(self[len(self)-mod:])
