class Node:
    def __init__(self, data):
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def insert_at_beg(self, newnode):
        if self.head is None:
            self.head= newnode
        else:
            self.head.prev=newnode
            newnode.next=self.head
            self.head=newnode

    def insert_at_end(self, newnode):
        if self.head==None:
            self.head=newnode
        else:
            currnode=self.head
            while currnode.next is not None:
                currnode=currnode.next
            currnode.next=newnode
            newnode.prev=currnode

    def insert_at_pos(self, pos, newnode):
        if pos==1:
            linkedlist.insert_at_beg()
        elif pos== linkedlist.length():
            linkedlist.insert_at_end()
        elif pos<0 or pos > linkedlist.length():
            print("Invalid Position")
        else:
            currnode=self.head
            tmp=self.head
            count=1
            while count!=pos:
                count+=1
                tmp= currnode
                currnode=currnode.next
            newnode.prev=tmp
            tmp.next=newnode
            newnode.next=currnode
            currnode.prev=newnode

    def del_at_beg(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp=self.head
            currnode=self.head.next
            currnode.prev=None
            temp.next=None
            self.head=currnode

    def del_at_end(self):
        currnode=self.head
        while currnode.next is not None:
            prevnode=currnode
            currnode=currnode.next
        currnode.prev= None
        prevnode.next= None

    def del_at(self,pos):
        if pos<1 or pos>linkedlist.length():
            print('invalid position')
        elif pos==1:
            linkedlist.del_at_beg()
        elif pos==linkedlist.length():
            linkedlist.del_at_end()
        else:
            currnode=self.head
            i=1
            while i!=pos:
                temp=currnode
                currnode=currnode.next
                i+=1
            temp.next=currnode.next
            currnode.next.prev=temp
            currnode.next=None
            currnode.prev=None

    def length(self):
            currnode=self.head
            count=0
            while currnode is not None:
                count+=1
                currnode=currnode.next
            return (count)

    def printlist(self):
        currnode=self.head
        while currnode is not None:
            print (currnode.data)
            currnode=currnode.next

n= int(input("enter the no of node "))
linkedlist=DoublyLinkedList()
for i in range(n):
    a=str(input("enter the data "))
    node=Node(a)
    #linkedlist.insert_at_beg(node)
    linkedlist.insert_at_end(node)
n=int(input("enter the position "))
#node=Node(input("enter the data "))
#linkedlist.insert_at_pos(n,node)"""
#linkedlist.del_at_beg()
#linkedlist.del_at_end()
linkedlist.del_at(n)
linkedlist.printlist()
print (linkedlist.length())
