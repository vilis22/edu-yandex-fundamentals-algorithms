import heapq


def main():
    n, k = map(int, input().split())
    discounts = list(map(int, input().split()))
    positive_discounts = [d for d in discounts if d > 0]
    best_discounts = heapq.nlargest(k, positive_discounts)
    print(sum(best_discounts))


if __name__ == "__main__":
    main()
