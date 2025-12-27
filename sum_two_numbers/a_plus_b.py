def add(x: int, y: int) -> int:
    return x + y


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(add(a, b))
