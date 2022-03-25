def main():
    di = {}
    answer = set()
    while True:
        str = input().split()
        if len(str) == 1:
            start = str[0]
            finish = input()
            break
        else:
            di.setdefault(str[0], set()).add(str[1])
            di.setdefault(str[1], set()).add(str[0])
    dest = di[start]
    di.pop(start)
    answer.update(dest)
    answer.update(set(start))
    while len(dest) != 0:
        new_dest = set()
        for elem in dest:
            if di.get(elem, -1) == -1:
                break
            new_dest.update(di[elem])
            di.pop(elem)
            new_dest.difference_update(answer)
        dest = new_dest
        answer.update(new_dest)
    if finish in answer:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
