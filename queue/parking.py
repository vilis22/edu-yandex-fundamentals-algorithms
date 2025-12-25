import heapq


def main():
    n, k = map(int, input().split())
    heap = []  # Min-heap для хранения времен окончания парковки
    total_parked = 0

    for _ in range(n):
        a, b = map(int, input().split())

        # Освободим место, где парковка закончилась до времени a
        while heap and heap[0] <= a:
            heapq.heappop(heap)

        # Есть свободное место
        if len(heap) < k:
            heapq.heappush(heap, b)
            total_parked += 1

    print(total_parked)


if __name__ == "__main__":
    main()
