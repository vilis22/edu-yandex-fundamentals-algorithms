import sys


def main():
    readline = sys.stdin.readline
    q = int(readline())
    dictionary = {}

    for _ in range(q):
        request = readline().split()

        match request[0]:
            case "1":
                dictionary[request[1]] = int(request[2])
            case "2":
                print(dictionary.get(request[1], -1))


if __name__ == "__main__":
    main()
