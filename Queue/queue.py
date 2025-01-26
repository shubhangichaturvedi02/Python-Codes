class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if not self.items:
            print("Queue is empty")

    def enqueue(self,val):
        self.items.append(val)

    def dequeue(self):
        if self.is_empty():
            print("Empty Queue")
        else:
            print(self.items.pop(0))
    
    def peek(self):
        if self.is_empty():
            print("Empty Queue")
        else:
            print(self.items[0])

    def show(self):
        print("Queue", self.items)


custom_queue = Queue()
custom_queue.enqueue(1)
custom_queue.enqueue(2)
custom_queue.enqueue(3)
custom_queue.enqueue(4)
custom_queue.enqueue(5)

custom_queue.show()
custom_queue.peek()
custom_queue.dequeue()
custom_queue.show()
