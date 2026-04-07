class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x: int) -> None:
        new_node = Node(x)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop(self) -> int:
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def peek(self) -> int:
        return self.head.data

    def empty(self) -> bool:
        return self.head is None


class MyStack:

    def __init__(self):
        self.queue = Queue()
        self.temp_queue = Queue()

    def push(self, x: int) -> None:
        self.temp_queue.push(x)
        while not self.queue.empty():
            self.temp_queue.push(self.queue.pop())
        self.queue, self.temp_queue = self.temp_queue, self.queue

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        return self.queue.peek()

    def empty(self) -> bool:
        return self.queue.empty()
