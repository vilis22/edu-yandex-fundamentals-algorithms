import sys
from collections import deque


def main():
    res = ""
    data = sys.stdin.read().split()
    deq = deque(data[1])

    while deq:
        if deq[0] <= deq[-1]:
            res += deq.popleft()
        else:
            res += deq.pop()

    sys.stdout.write(res)


if __name__ == "__main__":
    main()
