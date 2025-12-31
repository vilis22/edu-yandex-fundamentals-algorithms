import sys


def get_numbers():
    for line in sys.stdin:
        for word in line.split():
            yield int(word)


def main():
    numbers = get_numbers()
    next(numbers)
    max1, max2, max3 = -float("inf"), -float("inf"), -float("inf")
    min1, min2 = float("inf"), float("inf")

    for number in numbers:
        if number > max1:
            max1, max2, max3 = number, max1, max2
        elif number > max2:
            max2, max3 = number, max2
        elif number > max3:
            max3 = number

        if number < min1:
            min1, min2 = number, min1
        elif number < min2:
            min2 = number

    result = max(max1 * max2 * max3, max1 * min1 * min2)
    sys.stdout.write(f"{result}\n")


if __name__ == "__main__":
    main()
