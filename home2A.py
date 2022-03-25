import math

def main():
    flag = 1
    x, y, rad = map(int, input().split(","))

    while True:
        x_dot, y_dot = map(int, input().split(","))
        if x_dot == 0 and y_dot == 0:
            break
        if math.sqrt((x_dot - x) ** 2 + (y_dot - y) ** 2) > rad:
            print("NO")
            flag = 0
            break
    if flag == 1:
        print("YES")


if __name__ == "__main__":
    main()
