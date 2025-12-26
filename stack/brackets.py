def main():
    s = input()
    stack = []
    brackets = {")": "(", "]": "[", "}": "{"}

    for c in s:
        if c in "([{":
            stack.append(c)
        else:
            if not stack or brackets[c] != stack.pop():
                print("NO")
                return

    print("YES" if not stack else "NO")


if __name__ == "__main__":
    main()
