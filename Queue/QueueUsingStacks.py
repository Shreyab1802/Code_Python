class QueueUsingStacks:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, item):
        # Push the item into the enqueue stack
        self.stack_enqueue.append(item)

    def dequeue(self):
        if not self.stack_dequeue:
            # If dequeue stack is empty, transfer elements from enqueue stack
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())

        # Pop from the dequeue stack
        if self.stack_dequeue:
            return self.stack_dequeue.pop()
        else:
            # If both stacks are empty, return None
            return None

    def is_empty(self):
        # Queue is empty if both stacks are empty
        return not self.stack_enqueue and not self.stack_dequeue

    def size(self):
        # Size of the queue is the sum of the sizes of both stacks
        return len(self.stack_enqueue) + len(self.stack_dequeue)

    def peek(self):
        if not self.stack_dequeue:
            # If dequeue stack is empty, transfer elements from enqueue stack
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())

        # Peek from the dequeue stack
        if self.stack_dequeue:
            return self.stack_dequeue[-1]
        else:
            # If both stacks are empty, return None
            return None

# Example usage:
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Size of queue:", queue.size())  # Output: 3

print("Dequeue:", queue.dequeue())  # Output: 1
print("Dequeue:", queue.dequeue())  # Output: 2

queue.enqueue(4)
print("Peek:", queue.peek())  # Output: 3
print("Dequeue:", queue.dequeue())  # Output: 3

print("Is empty:", queue.is_empty())  # Output: False

print("Dequeue:", queue.dequeue())  # Output: 4
print("Is empty:", queue.is_empty())  # Output: True
