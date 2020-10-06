class Node(object):
    """docstring for Node."""
    def __init__(self):
        self.data =None
        self.next=None
    def set_data(self,data):
        self.data=data
    def get_data(self,data):
        return(self.data)
    def set_next(self,next):
        self.next=next
    def get_next(self,next):
        return(self.next)
    def has_next(self):
        return(self.next!=None)

n=int(input())
for i in range(n):
    a=input()
    node=Node()
    node.set_data(a)
    node.set_next(next)
    print(a)
    print(node)
    
