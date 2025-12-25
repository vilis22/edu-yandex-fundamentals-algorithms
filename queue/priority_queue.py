import heapq


def main():
    q = int(input())
    heap = []

    for _ in range(q):
        request = input().split()
        if request[0] == "1":
            heapq.heappush(heap, -int(request[1]))
            print(-heap[0])
        else:
            if heap:
                heapq.heappop(heap)
                if heap:
                    print(-heap[0])
                else:
                    print(-1)
            else:
                print(-1)


if __name__ == '__main__':
    main()
