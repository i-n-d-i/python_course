import math

def main():
    galaxy = set()
    while True:
        str = input()
        if len(str.split()) < 4:
            break
        a, b, c, name = str.split()
        lst = (name, float(a), float(b), float(c))
        galaxy.add(lst)
    answer = ['', '']
    maximum = 0
    galaxy = sorted(galaxy)
    for i in range(len(galaxy)):
        for j in range(i + 1, len(galaxy)):
            length = math.sqrt((galaxy[i][2] - galaxy[j][2]) ** 2 + (galaxy[i][1] - galaxy[j][1]) ** 2 + (galaxy[i][3] - galaxy[j][3]) ** 2)
            if length >= maximum:
                maximum = length
                answer[0] = galaxy[i][0]
                answer[1] = galaxy[j][0]
    print(answer[0], answer[1])

if __name__ == "__main__":
    main()
