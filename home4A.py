import sys

def divdigit(N):
    tmp = N
    answer = 0
    while tmp > 0:
        div = tmp % 10
        if div != 0 and N % div == 0:
            answer += 1
        tmp = tmp // 10
    return answer

exec(sys.stdin.read(), globals())
