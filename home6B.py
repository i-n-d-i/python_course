def main():
    seq = list(eval(input()))
    M = max(seq)
    s = set()
    M0 = int(M ** 0.5)
    for i in range(1, M0):
        i_sq = i * i
        M1 = int((M - i_sq) ** 0.5) + 1
        for j in range(i, M1):
            j_sq = j * j
            M2 = int((M - i_sq - j_sq) ** 0.5) + 1
            for k in range(j, M2):
                s.add(i_sq + j_sq + k * k)
    answer = len(s & set(seq))
    print(answer)


if __name__ == "__main__":
    main()
