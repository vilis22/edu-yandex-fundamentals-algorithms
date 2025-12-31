import sys
import heapq
from itertools import combinations
from math import prod


def main():
    data = list(map(int, sys.stdin.read().split()))[1:]
    print(data)
    top_max = heapq.nlargest(4, data)
    top_min = heapq.nsmallest(4, data)

    # todo здесь ошибка подумать надо с индексами
    candidates = top_max + top_min

    result = max(prod(combo) for combo in combinations(candidates, 4))
    sys.stdout.write(f"{result}\n")


if __name__ == "__main__":
    main()
