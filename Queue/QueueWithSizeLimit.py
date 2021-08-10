class Queue:
    def __init__(self,size) -> None:
        self.items=size * [None]
        self.maxSize=size
        self.top=-1
        self.start=-1

    def __str__(self) -> str:
        if self.isEmpty():
            return("Queue is Empty!")
        else:
            q=[str(x) for x in self.items]
            return ' '.join(q)

    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    def isFull(self):
        if self.start==0 and self.top+1==self.maxSize:
            return True
        elif self.top+1==self.start:
            return True
        else:
            return False
    def peek(self):
        if self.isEmpty() == True:
            return "Queue is Empty"
        else:
            return self.items[self.start]

    def enqueue(self,value):
        if self.isFull():
            print ("Queue is full, Cannot enter new element")
        else:
            if self.top+1==self.maxSize:
                self.top=0
            else:
                self.top+=1
                if self.start==-1:
                    self.start+=1 
            self.items[self.top]=value
            print ("Element is inserted at the top of Queue!!")   

    def dequeue(self):
        if self.isEmpty()==True:
            return("Queue is empty!!")
        else:
            firstElem= self.items[self.start]
            start=self.start
            if self.start==self.top:
                self.top=self.start=-1
            elif self.start+1==self.maxSize:
                self.start=0
            else:
                self.start+=1
            self.items[start]=None
            return firstElem

queue=Queue(3)
print(queue.isEmpty())
print(queue)
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())
print(queue)
queue.enqueue(3)
print(queue)
print(queue.start)
print(queue.top)
print(queue.isEmpty())
print(queue.isFull())
queue.enqueue(4)
print(queue)
print(queue.peek())