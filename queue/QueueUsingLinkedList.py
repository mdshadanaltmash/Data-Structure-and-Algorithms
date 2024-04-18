class Node:
    def __init__(self,value=None) -> None:
        self.value=value
        self.next=None

    def __str__(self) -> str:
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        currNode=self.head
        while currNode:
            yield currNode
            currNode=currNode.next
    
class Queue:
    def __init__(self) -> None:
        self.linkedlist=LinkedList()

    def __str__(self) -> str:
        values=[str(x) for x in self.linkedlist]
        return ' '.join(values)

    def enqueue(self,value):
        newNode=Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head=newNode
            self.linkedlist.tail=newNode
        else:
            self.linkedlist.tail.next=newNode
            self.linkedlist.tail=newNode

    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        else:
            return False

    def peek(self):
        if self.isEmpty():
            return "queue is Empty!!"
        else:
            return self.linkedlist.head

    def dequeue(self):
        if self.isEmpty():
            return "queue is Empty!!"
        else:
            tempNode=self.linkedlist.head
            if self.linkedlist.head==self.linkedlist.tail:
                self.linkedlist.head=None
                self.linkedlist.tail=None
            else:
                self.linkedlist.head=self.linkedlist.head.next
            return tempNode

    def delete(self):
        self.linkedlist.head=None
        self.linkedlist.tail=None

# queue=queue()
# print(queue.peek())
# print(queue.isEmpty())
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# print(queue.dequeue())
# print(queue)
# print(queue.peek())