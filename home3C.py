def main():
    answer = 0
    str = input()
    str = input()
    array = []
    while str[0] != '-':
        array.append([elem for elem in str] + ['.'])
        str = input()
    array.append(['.' for elem in str] + ['.'])
    for i in range(len(array) - 1):
        for j in range(len(array[i]) - 1):
            if array[i][j] == '#':
                if array[i][j+1] == '.' and array[i+1][j] == '.' and array[i+1][j+1] == '.':
                    answer +=1
    print(answer)

if __name__ == "__main__":
    main()
