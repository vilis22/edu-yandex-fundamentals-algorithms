def main():
    n = int(input())
    numbers = [int(x) for x in input().split()]
    min_prefix_val = numbers[0]
    min_prefix_idx = 0
    max_prefix_val = numbers[0]
    max_prefix_idx = 0
    min_diff = float("inf")
    max_diff = float("-inf")
    i1, j1 = 1, 2
    i2, j2 = 1, 2

    for j in range(1, n):
        diff_for_min = min_prefix_val - numbers[j]
        diff_for_max = max_prefix_val - numbers[j]

        if diff_for_min < min_diff:
            min_diff = diff_for_min
            i1 = min_prefix_idx + 1
            j1 = j + 1

        if diff_for_max > max_diff:
            max_diff = diff_for_max
            i2 = max_prefix_idx + 1
            j2 = j + 1

        if numbers[j] < min_prefix_val:
            min_prefix_val = numbers[j]
            min_prefix_idx = j

        if numbers[j] > max_prefix_val:
            max_prefix_val = numbers[j]
            max_prefix_idx = j

    print(i1, j1)
    print(i2, j2)


if __name__ == "__main__":
    main()
