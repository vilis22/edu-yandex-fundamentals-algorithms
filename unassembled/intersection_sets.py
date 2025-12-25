def main():
    n = int(input())
    first_set = set([int(x) for x in input().split()][1:])
    result = first_set

    for _ in range(n - 1):
        current_set = set([int(x) for x in input().split()][1:])
        result &= current_set

    print(len(result))


if __name__ == "__main__":
    main()
