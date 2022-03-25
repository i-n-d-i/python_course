def main():
    k = int(input())
    degree = 0
    answer = (k * (10 ** degree) - k ** 2) % (k * 10 - 1)
    while answer != 0:
        degree += 1
        answer = (k * (10 ** degree) - k ** 2) % (k * 10 - 1)
    answer = (k * (10 ** degree) - k ** 2) // (k * 10 - 1)
    answer = answer * 10 + k
    print(answer)

if __name__ == "__main__":
    main()
