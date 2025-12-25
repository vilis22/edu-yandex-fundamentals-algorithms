import sys
from collections import deque


def main():
    data = sys.stdin.read().split()

    if not data:
        return

    m = int(data[0])
    deq = deque()
    index = 1
    out_lines = []

    for _ in range(m):
        op = data[index]
        index += 1
        match op:
            case "1":
                x = int(data[index])
                index += 1
                deq.appendleft(x)
            case "2":
                x = int(data[index])
                index += 1
                deq.append(x)
            case "3":
                if deq:
                    deq.popleft()
            case "4":
                if deq:
                    deq.pop()

        if deq:
            out_lines.append(f"{deq[0]} {deq[-1]}")
        else:
            out_lines.append("-1")

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
