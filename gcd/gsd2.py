import sys
from math import gcd

if __name__ == "__main__":
    line = sys.stdin.read().strip().split()
    m, n = int(line[0]), int(line[1])
    result = gcd(m, n)
    sys.stdout.write(str(result) + "\n")
