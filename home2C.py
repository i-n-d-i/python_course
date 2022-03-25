import math

def main():
    N = int(input())
    for num in range(int(math.sqrt(N)) + 1, 1, -1):
        for degree in range(2, 10):
            if num ** degree == N:
                print("YES")
                return
    print("NO")

if __name__ == "__main__":
    main()
