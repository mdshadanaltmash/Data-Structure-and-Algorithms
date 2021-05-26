class Stack:
    def __init__(self):
        self.items=[]
        self.limit=int(input("enter the limit of Stack"))
    def push(self, data):
        if len(self.items)<self.limit:
            self.items.append(data)
        else:
            print('Stack Overflow')
    def length(self):
        return len(self.items)
    def is_Empty(self):
        return self.items==[]
    def pop(self):
        if self.is_Empty:
            return("Stack Underflow")
        else:
            return self.items[-1]
    def peek(self):
        if self.is_Empty():
            return("Stack is Empty")
        else:
            return(self.items[-1])
    def print_stack(self):
        if self.length()==0:
            print("Stack is Empty!!")
        else:
            for i in range(0,self.length()):
                print(self.items[self.length()-1-i])

s=Stack()
print("how many Data you want to insert in the Stack")
n=int(input())
print(s.pop())
print(s.peek())
for i in range(n):
    s.push(input('enter the Data'))
s.print_stack()
print(s.peek())
print(s.length())
