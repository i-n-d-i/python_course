import sys

def squares(w, h, *params):
    num = len(params)
    array = [['.' for i in range(w)] for j in range(h)]

    for m in range(num):
        x, y, s, c = params[m]
        for i in range(s):
            for j in range(s):
                array[i+y][j+x] = c

    for i in range(h):
        for j in range(w):
            print(array[i][j], end='')
        print()

exec(sys.stdin.read(), globals())
