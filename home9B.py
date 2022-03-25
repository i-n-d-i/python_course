class Tester:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, suite, allowed=[]):
        answer = 0
        for elem in suite:
            try:
                self.fun(*elem)
            except Exception as e:
                if type(e) in allowed:
                    answer = -1
                else:
                    answer = 1
                for ex in allowed:
                    if issubclass(type(e), ex):
                        answer = -1
                if answer == 1:
                    return answer
        return answer

T = Tester(int)
print(T([(12,), ("12", 16)], [ValueError, IndexError]))
print(T([(12,), ("12", 16), ("89", 8)], [ValueError, IndexError]))
print(T([(12,), ("12", 16), ("89", 8), (1, 1, 1)], [ValueError, IndexError]))
