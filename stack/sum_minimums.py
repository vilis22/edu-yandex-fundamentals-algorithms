from collections import deque


def main():
    n = int(input())
    k = int(input())
    a = list(map(int, input().split()))

    q = deque()
    total = 0

    for i in range(n):
        while q and a[q[-1]] > a[i]:
            q.pop()

        q.append(i)

        if q[0] <= i - k:
            q.popleft()

        if i >= k - 1:
            total += a[q[0]]

    print(total)


if __name__ == "__main__":
    main()
