class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data: int):
        """Добавляет узел в начало односвязного списка"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_after(self, index: int, data: int):
        """Добавляет узел после индекса (индексация с 1)"""
        current = self.head

        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next

        if current is None:
            raise IndexError("Index out of range")

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def print_by_index(self, index: int):
        """Выводит узел по индексу (индексация с 1)"""
        if self.head is None:
            raise IndexError("List is empty")

        current = self.head

        for _ in range(index - 1):
            if current.next is None:
                raise IndexError("Index out of range")
            current = current.next

        print(current.data)

    def remove_by_index(self, index: int):
        """Удаляет узел по индексу (индексация с 1)"""
        if self.head is None:
            raise IndexError("List is empty")

        if index == 1:
            self.head = self.head.next
            return

        current = self.head

        for _ in range(index - 2):
            if current.next is None:
                raise IndexError("Index out of range")
            current = current.next

        if current.next is None:
            raise IndexError("Index out of range")

        current.next = current.next.next

    def print_list(self):
        elements = []
        current = self.head

        while current:
            elements.append(str(current.data))
            current = current.next

        print(" → ".join(elements) + " → None")


def main():
    lst = LinkedList()
    q = int(input())

    for _ in range(q):
        request = [int(x) for x in input().split()]

        match request[0]:
            case 1:
                if request[1] == 0:
                    lst.add_first(request[2])
                else:
                    lst.add_after(request[1], request[2])
            case 2:
                lst.print_by_index(request[1])
            case 3:
                lst.remove_by_index(request[1])
            case _:
                raise ValueError("Invalid request")


if __name__ == "__main__":
    main()
