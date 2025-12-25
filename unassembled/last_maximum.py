import sys


def main():
    input = sys.stdin.readline
    n = int(input())
    numbers = [int(x) for x in input().split()]
    max_value = float("-inf")
    last_max_index = -1

    for i, num in enumerate(numbers):
        if num >= max_value:
            max_value = num
            last_max_index = i

    numbers.pop(last_max_index)
    print(*numbers)


if __name__ == "__main__":
    main()
