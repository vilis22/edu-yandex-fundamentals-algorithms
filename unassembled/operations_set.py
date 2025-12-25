def main():
    q = int(input())
    set_numbers = set()

    for _ in range(q):
        request = [int(x) for x in input().split()]
        match request[0]:
            case 1:
                set_numbers.add(request[1])
            case 2:
                if request[1] in set_numbers:
                    print(1)
                else:
                    print(0)


if __name__ == "__main__":
    main()
