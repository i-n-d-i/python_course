from itertools import groupby
import sys


def LookSay():
    s = [1]
    yield(s[0])
    while True:
        ss = groupby(s)
        s = []
        while True:
            try:
                Next = next(ss)
                elem = list(Next[1])
                s.append(len(elem))
                s.append(elem[0])
                yield len(elem)
                yield elem[0]
            except StopIteration:
                break

exec(sys.stdin.read(), globals())
