def main():
    n, q = (int(x) for x in input().split())
    a = [int(x) for x in input().split()]
    index_map = {}

    for i, val in enumerate(a):
        if val not in index_map:
            index_map[val] = i + 1

    for _ in range(q):
        x = int(input())
        print(index_map.get(x, -1))


if __name__ == "__main__":
    main()
