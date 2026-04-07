class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, head: "Node"=None):
        self.head = head

    def push(self, x):
        probe = self.head
        self.head = Node(x)
        self.head.next = probe

    def pop(self):
        probe = self.head.data
        self.head = self.head.next
        return probe

    def peek(self):
        return self.head.data

    def empty(self):
        return self.head is None

class MyQueue:

    def __init__(self):
        self.lifo_stack = Stack()
        self.out_stack = Stack()


    def push(self, x: int) -> None:
        while not self.out_stack.empty():
            self.lifo_stack.push(self.out_stack.pop())

        self.lifo_stack.push(x)

        while not self.lifo_stack.empty():
            self.out_stack.push(self.lifo_stack.pop())

    def pop(self) -> int:
        return self.out_stack.pop()

    def peek(self) -> int:
        return self.out_stack.peek()

    def empty(self) -> bool:
        return self.lifo_stack.empty() and self.out_stack.empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
