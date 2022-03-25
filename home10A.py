from functools import wraps

def cast(param):
    def decorator(fun):
        @wraps(fun)
        def newfun(*args):
            return (param)(fun(*args))
        return newfun
    return decorator

@cast(int)
def fun(a, b):
    return a * 2 + b
    
print(fun(12, 34) * 2)
print(fun("12", "34") * 2)
print(fun(12.765, 34.654) * 2)
