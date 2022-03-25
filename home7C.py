import sys
import random
import types

def randomes(seq):
    if isinstance(seq, types.GeneratorType):
        my_seq = [list(elem) for elem in seq]
    else:
        my_seq = seq
    num = len(my_seq)
    while True:
        for i in range(num):
            elem = my_seq[i]
            yield random.randint(elem[0], elem[1])


exec(sys.stdin.read(), globals())
