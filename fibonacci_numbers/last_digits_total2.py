import sys


def fibonacci_last_digit_sum(num: int) -> int:
    pisano_period = 60
    num = num % pisano_period

    if num <= 1:
        return num

    a, b = 0, 1
    total_sum = 1

    for i in range(2, num + 1):
        a, b = b, (a + b) % 10
        total_sum = (total_sum + b) % 10

    return total_sum


if __name__ == "__main__":
    line = sys.stdin.read().strip().split()
    m, n = int(line[0]), int(line[1])
    result = (fibonacci_last_digit_sum(n) - fibonacci_last_digit_sum(m - 1)) % 10
    sys.stdout.write(str(result) + "\n")
