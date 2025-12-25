import heapq


def main():
    n = int(input())
    tickets = []

    for _ in range(n):
        ticket = input().split()
        heapq.heappush(tickets, (-int(ticket[1]), int(ticket[0])))

    employee_1 = 0
    employee_2 = 0

    while tickets:
        if employee_1 <= employee_2:
            ticket = heapq.heappop(tickets)
            employee_1 += ticket[1]
        else:
            ticket = heapq.heappop(tickets)
            employee_2 += ticket[1]

    print(max(employee_1, employee_2))


if __name__ == '__main__':
    main()
