
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class LinkedListStack:
    def __init__(self,head=None) -> None:
        self.head=head

    def push(self,data):
        data=Node(data)
        if self.head is None:
            self.head=data
        else:
            data.next=self.head
            self.head=data
    
    def pop(self):
        if self.head is None:
            print ("Stack Underflow")
        else:
            tmp=self.head
            if tmp.next:
                self.head=tmp.next
                tmp.next=None
                return tmp.data
            else:
                self.head=None
                return tmp.data
    
    def peek(self):
        if self.isEmpty():
            return "Stack Underflow"
        else:
            return self.head.data

    def print_stack(self):
        tmp=self.head
        while tmp:
            print(tmp.data)
            tmp=tmp.next
    
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    
    def length(self):
        count=0
        tmp=self.head
        while tmp:
            count+=1
            tmp=tmp.next
        return count


s=LinkedListStack()
n=5
print(s.length())
print(s.isEmpty())
for i in range(n):
    s.push(i)
s.print_stack()
print(s.pop())
s.print_stack()
print(s.length())
print(s.isEmpty())
print(s.peek())
