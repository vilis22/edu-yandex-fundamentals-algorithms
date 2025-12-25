def main():
    n = int(input())
    sets = []
    for _ in range(n):
        data = list(map(int, input().split()))
        sets.append(set(data[1:]))

    # Находим ядро - пересечение всех множеств
    core = sets[0].copy()

    for i in range(1, n):
        core &= sets[i]

    # Проверим, что лепестки попарно не пересекаются (S_i ∩ S_j = core для всех пар)
    seen = set()
    petal_sizes = []

    for s in sets:
        petal = s - core

        for elem in petal:
            if elem in seen:
                print("NO")
                return
            seen.add(elem)

        petal_sizes.append(len(petal))

    print("YES")
    print(len(core))
    print(" ".join(map(str, petal_sizes)))


if __name__ == "__main__":
    main()
