import sys


def fibonacci_mod(n: int, m: int) -> int:
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b) % m
    return b


def pisano_period(m: int) -> int:
    a, b = 0, 1
    period = 0

    while True:
        a, b = b, (a + b) % m
        period += 1

        if a == 0 and b == 1:
            return period


if __name__ == "__main__":
    input_n, input_m = map(int, sys.stdin.read().split())
    p = pisano_period(input_m)
    sys.stdout.write(str(fibonacci_mod(input_n % p, input_m)) + "\n")