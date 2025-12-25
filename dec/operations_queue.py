from collections import deque


def main():
    q = int(input())
    queue = deque()

    for _ in range(q):
        request = list(map(int, input().split()))

        match request[0]:
            case 1:
                queue.append(request[1])
            case 2:
                queue.popleft()

        if not queue:
            print(-1)
        else:
            print(queue[0])


if __name__ == "__main__":
    main()
