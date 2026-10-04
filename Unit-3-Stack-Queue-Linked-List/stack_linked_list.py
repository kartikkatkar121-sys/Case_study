class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data if self.top else None

    def display(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next


if __name__ == "__main__":
    stack = Stack()
    stack.push("Type Hello")
    stack.push("Type World")
    stack.push("Delete World")

    print("Stack (Top to Bottom):")
    stack.display()
    print("\nUndo:", stack.pop())
    print("Current Top:", stack.peek())
