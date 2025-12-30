import heapq
import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    two_largest = heapq.nlargest(2, data[1:])
    sys.stdout.write(f"{two_largest[0] * two_largest[1]}\n")


if __name__ == "__main__":
    main()
