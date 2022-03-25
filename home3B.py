def main():
    str = eval(input())
    str = sorted(str)

    begin = str[0][0]
    end = str[0][1]
    answer = 0
    for i in range(1, len(str)):
        if str[i][0] <= end <= str[i][1]:
            end = str[i][1]
        elif end < str[i][0]:
            answer = answer + end - begin
            begin = str[i][0]
            end = str[i][1]
    answer = answer + end - begin
    print(answer)


if __name__ == "__main__":
    main()
