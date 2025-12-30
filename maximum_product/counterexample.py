import sys


def is_there_input(n: int) -> bool:
    return 2 * n - 3 > 1.5 * n


if __name__ == "__main__":
    n = int(sys.stdin.read())

    if is_there_input(n):
        sys.stdout.write("Yes\n")
        counterexample = list(range(n, 0, -1))
        sys.stdout.write(" ".join(map(str, counterexample)) + "\n")
    else:
        sys.stdout.write("No\n")
