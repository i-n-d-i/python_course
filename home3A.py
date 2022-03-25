def main():
    m, n = map(int, input().split(","))
    x_add, y_add = 0, 1
    x, y = 0, 0
    answer = [[None] * m for elem in range(n)]
    for elem in range(0, n * m):
        elem = elem % 10
        answer[x][y] = elem
        x_new, y_new = x + x_add, y + y_add
        if 0 <= x_new < n and 0 <= y_new < m and answer[x_new][y_new] == None:
            x, y = x_new, y_new
        else:
            y_add, x_add = -x_add, y_add
            x, y = x + x_add, y + y_add
    for x in range(n):
        for y in range(m):
            print(answer[x][y], end = ' ')
        print()


if __name__ == "__main__":
    main()
