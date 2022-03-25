def main():
    main_str = input()
    pattern_str = input().split("@")

    num = main_str.count(pattern_str[0])
    size = len(pattern_str)

    position = main_str.find(pattern_str[0])
    answer = position
    if answer == -1:
        print("-1")
        return

    for j in range(num):
        for i in range(1, size):
            position += len(pattern_str[i-1]) + 1
            pos = main_str.find(pattern_str[i], position)
            if pos != position:
                position = main_str.find(pattern_str[0], answer + 1)
                answer = position
                break
            if pos == position and i == size-1:
                print(answer)
                return
        if answer == -1:
            print("-1")
            return
    print(answer)


if __name__ == "__main__":
    main()
