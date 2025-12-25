from collections import deque


def main():
    q = int(input())
    stack = deque()

    for _ in range(q):
        query = input().split()

        if query[0] == "1":
            stack.append(int(query[1]))
        elif query[0] == "2":
            stack.pop()

        print(stack[-1] if stack else -1)


if __name__ == "__main__":
    main()
