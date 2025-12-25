import sys
from fractions import Fraction


def main():
    readline = sys.stdin.readline
    n = int(readline())
    fractions = {}

    for _ in range(n):
        num, den = map(int, readline().split())
        fractions[Fraction(num, den)] = fractions.get(Fraction(num, den), 0) + 1

    max_value = max(fractions.values())
    min_key = min(key for key, value in fractions.items() if value == max_value)
    print(min_key.numerator, min_key.denominator)


if __name__ == "__main__":
    main()
