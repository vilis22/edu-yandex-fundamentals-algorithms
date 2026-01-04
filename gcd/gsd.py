import sys


def gcd(a, b):
    while a > 0 and b > 0:
        if a >= b:
            a %= b
        else:
            b %= a

    return max(a, b)


if __name__ == "__main__":
    line = sys.stdin.read().strip().split()
    m, n = int(line[0]), int(line[1])
    result = gcd(m, n)
    sys.stdout.write(str(result) + "\n")
