import sys

def superposition(funmod, funseq):
    answer = []
    n = len(funseq)
    for i in range(n):
        def func(x, j = i):
            return funmod(funseq[j](x))
        answer.append(func)
    return answer


exec(sys.stdin.read(), globals())
