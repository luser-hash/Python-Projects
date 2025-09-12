"""
    A Queue is a linear Data Structure that follows First-In-First-Out or FIFI principle.
    That means the first element that added to the list will remove first.
    Queue Operations:
        1. Enqueue -> Add an element to the end of the queue.
        2. Dequeue -> Remove the element of the the front.
        3. Front -> View the front element without removing it. 
        4. isEmpty -> Check if empty or not
    
    Examples of Queue:
        1. Printer Queue
        2. Customer service
        3. Call Center
        4. Task Scheduling
"""

# Queue with OOP
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return " Queue is Empty."
        return self.queue.pop(0)
    
    def front(self):
        if self.isEmpty():
            return " Queue is Empty."
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
myQueue = Queue()

myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)

print('Enqueue: ', myQueue.queue)
print('Dequeue: ', myQueue.dequeue())
print('Front: ', myQueue.front())
print('Is Empty: ', myQueue.isEmpty())
print('Size: ', myQueue.size())