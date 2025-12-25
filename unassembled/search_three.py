import sys


def main():
    readline = sys.stdin.readline
    n = int(readline())
    numbers = [int(x) for x in readline().split()]
    count = {}

    for num in numbers:
        count[num] = count.get(num, 0) + 1

    items = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    top3 = sorted([k for k, v in items[:3]])
    print(*top3)

if __name__ == "__main__":
    main()
