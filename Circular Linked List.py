class Node():
    def __init__(self, data):
        self.data=data
        self.next=None

class CircularLinkedList():
    def __init__(self):
        self.head=None

    def insert_at_beg(self, newnode):
        currnode=self.head
        newnode.next=self.head
        if self.head==None:
            newnode.next=newnode
        else:
            while currnode.next!=self.head:
                currnode=currnode.next
            currnode.next=newnode
        self.head=newnode

    def insert_at_end(self, newnode):
        if not self.head:
            self.head=newnode
            newnode.next=self.head
        else:
            currnode=self.head
            while currnode.next!=self.head:
                currnode=currnode.next
            currnode.next=newnode
            newnode.next=self.head

    def insert_at(self,pos,newnode):
        currnode=self.head
        count=1
        if currnode==None or  pos==1:
            linkedlist.insert_at_beg(newnode)
        elif pos==linkedlist.length():
            linkedlist.insert_at_end(newnode)
        elif pos<0 or pos > linkedlist.length():
            print('invalid position')
        else:
            while count!=pos:
                prevnode=currnode
                currnode=currnode.next
                count+=1
            prevnode.next=newnode
            newnode.next=currnode

    def del_at_end(self):
        currnode=self.head
        while currnode.next!=self.head:
            prevnode=currnode
            currnode=currnode.next
        prevnode.next=self.head
        currnode.next=None

    def del_at_beg(self):
        currnode=self.head
        tmp=self.head
        while currnode.next!=self.head:
            currnode=currnode.next
        self.head=self.head.next
        currnode.next=self.head
        tmp.next=None

    def del_at(self,pos):
        currnode=self.head
        count=1
        if pos<1 or pos>linkedlist.length():
            print('invalid position')
        elif pos==1:
            linkedlist.del_at_beg()
        elif pos==linkedlist.length():
            linkedlist.del_at_end()
        else:
            while count!=pos:
                prevnode=currnode
                currnode=currnode.next
                count+=1
            prevnode.next=currnode.next

    def length(self):
        currnode=self.head
        count=1
        while currnode.next!=self.head:
            count+=1
            currnode=currnode.next
        return(count)

    def printlist(self):
        currnode=self.head
        if currnode==None:
            print('List is Empty')
        else:
            while True:
                print(currnode.data)
                currnode=currnode.next
                if currnode==self.head:
                    break

n=int(input("enter the no of node "))
linkedlist=CircularLinkedList()
for i in range(n):
    node=Node(input("enter the data "))
    linkedlist.insert_at_beg(node)
    #linkedlist.insert_at_end(node)
"""n=int(input("enter the position "))
node=Node(input("enter the data "))
linkedlist.insert_at(n,node)"""
#linkedlist.del_at_end()
#linkedlist.del_at_beg()
print('Enter the position to delete the data ')
linkedlist.del_at(input())
linkedlist.printlist()
print(linkedlist.length())
