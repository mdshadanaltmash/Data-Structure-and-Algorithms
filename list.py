class Node(object):
    def __init__(self, data):
        self.data=data
        self.next=None
class LinkedList(object):
    def __init__(self):
        self.head=None

    def length(self):
        currnode=self.head
        count=0
        while currnode is not None:
            count+=1
            currnode=currnode.next
        return count

    def insert_at_end(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode=lastnode.next
            lastnode.next=newnode

    def insert_at_beg(self,newnode):
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode

    def insert_at(self,pos,newnode):
        if pos<0 or pos>linkedlist.length():
            print("invalid pos")
        elif pos==0:
            insert_at_beg(newnode)
        elif pos==linkedlist.length():
            insert_at_end(newnode)
        else:
            i=1
            currnode=self.head
            while i<pos-1:
                i+=1
                currnode=currnode.next
            newnode.next=currnode.next
            currnode.next=newnode
    def del_at_beg(self):
        if linkedlist.length==0:
            print("linked list is Empty")
        else:
            currnode=self.head
            self.head=currnode.next

    def del_at_end(self):
        if linkedlist.length==0:
            print('linked list is Empty')
        elif linkedlist.length==1:
            self.head=None
        else:
            i=1
            currnode=self.head
            while i<(linkedlist.length()-1):
                currnode=currnode.next
                i+=1
            currnode.next=None

    def delat_end(self):
        currnode=self.head
        prevnode=self.head
        if currnode==None:
            print('linked list is Empty')
        elif currnode.next==None:
            currnode=None
        else:
            while currnode.next!=None:
                prevnode=currnode
                currnode=currnode.next
            prevnode.next=None

    def del_bw(self,data):
        #invalid data is missing
        currnode=self.head
        prevnode=self.head
        if currnode==None:
            print ("list is Empty")
        elif currnode.next==None:
            linkedlist.del_at_beg()
        else:
            while currnode.data!=data:
                prevnode=currnode
                currnode=currnode.next
                if currnode==None:
                    print('Data is not in the list')
                    return
            prevnode.next=currnode.next
            currnode.next=None



    def printlist(self):
        currnode= self.head
        while True:
            if currnode is None:
                break
            print(currnode.data)
            currnode=currnode.next


n=int(input("enter the no of node "))
linkedlist=LinkedList()
for i in range(n):
    node=Node(input("enter the data "))
    #linkedlist.insert_at_beg(node)
    linkedlist.insert_at_end(node)
linkedlist.printlist()
n=int(input("enter the position "))
node=Node(input("enter the data "))
linkedlist.insert_at(n,node)
#linkedlist.del_at_beg()
#linkedlist.del_at_end()
#linkedlist.delat_end()
data=input("enter the data to be deleted from the linked list")
linkedlist.del_bw(data)
linkedlist.printlist()
print(linkedlist.length())
