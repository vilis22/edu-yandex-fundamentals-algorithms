from collections import deque


def main():
    n = int(input())
    warrior_forces = deque(map(int, input().split()))

    for _ in range(n - 3):
        first, second, third = (
            warrior_forces.popleft(),
            warrior_forces.popleft(),
            warrior_forces.pop(),
        )
        if first > second and first > third:
            if second > third:
                warrior_forces.appendleft(second)
            else:
                warrior_forces.append(third)
            warrior_forces.appendleft(first)
        elif second > first and second > third:
            if first > third:
                warrior_forces.append(first)
            else:
                warrior_forces.appendleft(third)
            warrior_forces.appendleft(second)
        else:
            if first > second:
                warrior_forces.appendleft(first)
            else:
                warrior_forces.appendleft(second)
            warrior_forces.appendleft(third)

    print(*(warrior for warrior in warrior_forces if warrior != min(warrior_forces)))


if __name__ == "__main__":
    main()
