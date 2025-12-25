import sys


def main():
    readline = sys.stdin.readline
    n = int(readline())
    numbers = [int(x) for x in readline().split()]
    remaining_numbers = [numbers[0]]

    for i in range(1, n - 1):
        if numbers[i] >= numbers[i - 1] or numbers[i] >= numbers[i + 1]:
            remaining_numbers.append(numbers[i])

    remaining_numbers.append(numbers[-1])
    print(len(remaining_numbers))
    print(*remaining_numbers)


if __name__ == "__main__":
    main()
