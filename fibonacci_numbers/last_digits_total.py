import sys


def fibonacci_last_digit_sum(num: int) -> int:
    if num <= 1:
        return num

    # Последние цифры чисел Фибоначчи повторяются с периодом (Pisano period по модулю 10)
    # Для mod 10 период = 60
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
    line = sys.stdin.read().strip()
    n = int(line)
    sys.stdout.write(str(fibonacci_last_digit_sum(n)) + "\n")
