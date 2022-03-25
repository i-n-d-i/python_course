import sys

def BinPow(a, N, f):
    answer = a
    N -= 1
    while N:
        if N & 1:
            answer = f(answer,a)
        a = f(a, a)
        N >>= 1
    return answer

exec(sys.stdin.read(), globals())
