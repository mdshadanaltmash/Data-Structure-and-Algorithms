class Queue:
    def __init__(self) -> None:
        self.items=[]
    
    def __str__(self) -> str:
        q=[str(x) for x in self.items]
        return ' '.join(q)

    def isEmpty(self):
        if self.items==[]:
            return True
        else:
            return False
    def peek(self):
        if self.isEmpty() == True:
            return "queue is Empty"
        else:
            return self.items[0]
    
    def enqueue(self,value):
        self.items.append(value)
        print ("Item has been inserted at the end of the queue.")
    
    def dequeue(self):
        if self.isEmpty() == True:
            return "queue is Empty"
        else:
            return self.items.pop(0)
    
queue=Queue()
print(queue.isEmpty())
print(queue.peek())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.isEmpty())
print(queue.peek())
print(queue)
print(queue.dequeue())
print(queue)
