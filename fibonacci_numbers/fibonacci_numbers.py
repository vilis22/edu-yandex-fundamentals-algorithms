import sys


def fibonacci(n: int) -> int:
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    line = sys.stdin.read().strip()
    n = int(line)
    sys.stdout.write(str(fibonacci(n)) + '\n')
