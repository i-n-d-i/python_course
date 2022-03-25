from functools import update_wrapper

class sizer:
    def __init__(self, cls):
        self = update_wrapper(self, cls)
        self.cls = cls
        self.type = cls.__bases__[0]

    def __call__(self, *args, **kwargs):
        if len(args) == 0:
            self.arg = args
            self.cls.size = self.size
            return self.cls()
        self.arg = (self.type)(args[0])
        self.cls.size = self.size
        return self.cls(self.arg)

    @property
    def size(self):
        if hasattr(self.cls, "__len__"):
            return self.cls.__len__(self.arg)
        if hasattr(self.cls, "__abs__"):
            return self.cls.__abs__(self.arg)
        return 0


@sizer
class S(str):
    pass

@sizer
class N(complex):
    pass

@sizer
class E(Exception):
    pass

for obj in S("QWER"), N(3+4j), E("Exceptions know no lengths!"):
    print(obj, obj.size)
