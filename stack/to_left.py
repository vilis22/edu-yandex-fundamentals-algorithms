def main():
    n = int(input())
    a = list(map(int, input().split()))

    stack = []
    visibility = [0] * n

    for i in range(n):
        while stack and a[stack[-1]] < a[i]:
            stack.pop()

        if not stack:
            visibility[i] = i
        else:
            visibility[i] = i - stack[-1] - 1

        stack.append(i)

    print(*visibility)


if __name__ == "__main__":
    main()
