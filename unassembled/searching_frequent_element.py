import sys


def main():
    readline = sys.stdin.readline
    n = int(readline())
    numbers = [int(x) for x in readline().split()]
    count = {}

    for num in numbers:
        count[num] = count.get(num, 0) + 1

    max_value = max(count.values())
    min_key = min(key for key, value in count.items() if value == max_value)
    print(min_key)


if __name__ == "__main__":
    main()
