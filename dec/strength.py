import sys
from collections import deque


def main():
    data = sys.stdin.read().split()
    power = deque(map(int, data[1:]))

    while len(power) > 3:
        tail = power.pop()
        head = power.popleft()
        body = power.popleft()

        if tail == min(head, body, tail):
            if head > body:
                power.appendleft(body)
                power.appendleft(head)
            else:
                power.appendleft(head)
                power.appendleft(body)
        elif tail == max(head, body, tail):
            if head > body:
                power.appendleft(head)
            else:
                power.appendleft(body)
            power.appendleft(tail)
        else:
            power.append(tail)
            if head > body:
                power.appendleft(head)
            else:
                power.appendleft(body)

    final = [warrior for warrior in power if warrior != min(power)]
    sys.stdout.write(f"{final[0]} {final[1]}\n")


if __name__ == "__main__":
    main()
