import sys
import heapq

def main():
    data = sys.stdin.read().split()
    n, k = map(int, data[:2])
    idx = 2
    heap = [(0, i) for i in range(k)]
    heapq.heapify(heap)
    result = []

    for _ in range(n):
        t_i = int(data[idx])
        d_i = int(data[idx + 1])
        idx += 2
        ready_time, server = heapq.heappop(heap)
        start = max(t_i, ready_time)
        finish = start + d_i
        heapq.heappush(heap, (finish, server))
        result.append(str(finish))

    sys.stdout.write(" ".join(result))

if __name__ == "__main__":
    main()
