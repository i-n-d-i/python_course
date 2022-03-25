def main():
    number = int(input())
    tmp = number
    reverse = 0

    while tmp > 0:
        div = tmp % 10
        reverse = reverse * 10 + div
        tmp = tmp // 10
    if reverse == number:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
