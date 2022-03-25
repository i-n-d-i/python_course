from functools import update_wrapper

class counter:
    def __init__(self, fun):
        self = update_wrapper(self, fun)
        self.count = 0
        self.function = fun

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.function(*args, **kwargs)

    def counter(self):
        return self.count

@counter
def fun(a, b):
    return a + b

print(fun.counter())
res = sum(fun(i, i + 1) for i in range(5))
print(fun.counter(), res)
