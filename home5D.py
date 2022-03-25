import math

def main():
    string1 = '{:{align1}{width1}} * {:{align2}{width2}} = {:{align3}{width3}}'
    string2 = '{:{align1}{width1}} * {:{align2}{width2}} = {:{align3}{width3}} | '

    n, m = map(int, input().split(","))
    mul = n * n
    size = len(str(n)) * 2 + len(str(mul)) + 6
    num = m // size
    while num * size + (num - 1) * 3 > m:
        num -= 1
    list = ["=" for i in range(m)]
    line = ''.join(list)

    l1 = len(str(n))
    l2 = len(str(mul))
    for m in range(math.ceil(n / num)):
        print(line)
        for i in range(1, n + 1):
             for j in range(1 + num * m, num + 1 + num * m):
                 if j > n:
                     continue
                 if j % num == 0 or j == n:
                     print(string1.format(j, i, i * j, align1 ='>', width1 = l1, align2 = '<', width2 = l1, align3 ='<', width3 = l2), end="")
                     print()
                 else:
                     print(string2.format(j, i, i * j, align1 ='>', width1 = l1, align2 = '<', width2 = l1, align3 ='<', width3 = l2), end="")
    print(line)

if __name__ == "__main__":
    main()
