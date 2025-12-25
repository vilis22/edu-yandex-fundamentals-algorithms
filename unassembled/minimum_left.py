import sys


def main():
    input = sys.stdin.readline
    n = int(input())
    numbers = [int(x) for x in input().split()]
    current_min = numbers[0]
    print(current_min, end="")

    for i in range(1, n):
        num = numbers[i]
        if num < current_min:
            current_min = num
        print(f" {current_min}", end="")


if __name__ == "__main__":
    main()
