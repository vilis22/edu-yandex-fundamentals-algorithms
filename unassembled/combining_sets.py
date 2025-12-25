def main():
    n = int(input())
    set_numbers = set()

    for _ in range(n):
        request = [int(x) for x in input().split()]
        set_numbers.update(request[1:])

    print(len(set_numbers))


if __name__ == "__main__":
    main()
