import itertools
import sys

def chainslice(begin, end, *seq):
    my_seq = itertools.chain(*seq)
    my_list = list(itertools.islice(my_seq, begin, end))
    for i in range(end - begin):
        yield my_list[i]

exec(sys.stdin.read(), globals())
