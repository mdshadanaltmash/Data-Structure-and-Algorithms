class Stack:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        if len(self.items) ==0:
            return True
        else:
            return False
    def length(self):
        return len(self.items)
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow")
        else:
            return (self.items.pop())
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.items[-1]
    def print_stack(self):
        if self.isEmpty():
            print("Stack is Empty")
            
        else:
            for i in range(0,self.length()):
                print(self.items[self.length()-1-i])


    
n=10
stk=Stack()
for i in range(n):
    stk.push(i)
stk.print_stack()
print(stk.isEmpty())
print(stk.peek())
print(stk.length())
print(stk.pop())
print(stk.peek())
print(stk.length())