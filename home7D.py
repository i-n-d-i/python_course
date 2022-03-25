import sys

def joinseq(*seq):
    my_seq = [list(elem) for elem in seq]
    my_seq.sort()
    num = 0
    for elem in my_seq:
        num += len(elem)
    for i in range(num):
        if not my_seq[0]:
            my_seq = my_seq[1:]
        yield my_seq[0][0]
        my_seq[0] = my_seq[0][1:]
        my_seq.sort()

exec(sys.stdin.read(), globals())
