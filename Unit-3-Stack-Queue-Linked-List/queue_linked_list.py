class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)
        if self.rear is None:
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.front is None:
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def display(self):
        current = self.front
        while current:
            print(current.data)
            current = current.next


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue("Save File")
    queue.enqueue("Print Document")
    queue.enqueue("Upload File")

    print("Queue (Front to Rear):")
    queue.display()
    print("\nProcessed:", queue.dequeue())
