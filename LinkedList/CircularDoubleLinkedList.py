class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class CircularDLL:
    def __init__(self):
        self.head=None

    def print_list(self):
        curr=self.head
        if curr is None:
            print("Circurlar Double Linked List is empty!!!")
        while curr:
            print (curr.data,end='<-->')
            curr=curr.next
            if curr==self.head:
                break
        print()
    
    def list_length(self):
        if self.head is None:
            return 0
        count=1
        curr=self.head
        while curr.next!=self.head:
            count+=1
            curr=curr.next
        return count
    
    def insert_at_beg(self,node):
        node=Node(node)
        curr=self.head
        if self.head is None:
            self.head=node
            node.next=node
            node.prev=node
        else:
            while curr.next!=self.head:
                curr=curr.next
            curr.next=node
            node.prev=curr
            node.next=self.head
            self.head.prev=node
            self.head=node
    
    def insert_at_end(self,node):
        node=Node(node)
        curr=self.head
        if self.head is None:
            self.head=node
            node.next=node
            node.prev=node
        while curr.next!=self.head:
            curr=curr.next
        node.next=curr.next
        node.prev=curr
        curr.next=node
        self.head.prev=node

    def insert_at_pos(self,node,pos):
        if pos==0:
            self.insert_at_beg(node)
        elif pos==-1 or pos==self.list_length():
            self.insert_at_end(node)
        elif pos>0 and pos<self.list_length():
            node=Node(node)
            idx=1
            curr=self.head
            while idx!=pos:
                idx+=1
                curr=curr.next
            curr.next.prev=node
            node.next=curr.next
            node.prev=curr
            curr.next=node
        else:
            print("Invalid Position!!")

    def get_pos_of(self,data):
        idx=0
        curr=self.head
        while curr:
            if curr.data==data:
                return idx
            idx+=1
            curr=curr.next
            if curr==self.head:
                break
        return None

    def get_val_at(self,pos):
        if self.head is None:
            return None
        curr=self.head
        idx=0
        if pos<0 or pos>self.list_length():
            return None
        else:
            while idx!=pos:
                curr=curr.next
                idx+=1
            return curr.data

    def del_at_beg(self):
        if self.head is None:
            print("List is Empty")
        elif self.head.next is None:
            self.head=None
        else:
            tmp=curr=self.head
            
            while curr.next!=self.head:
                curr=curr.next
            tmp=tmp.next
            tmp.prev=curr
            curr.next=tmp
            self.head=tmp
            

    def del_at_end(self):
        if self.head is None:
            print("List is Empty")
        else:
            curr=prev=self.head
            while curr.next!=self.head:
                prev=curr
                curr=curr.next
            prev.next=self.head
            self.head.prev=prev
    def del_at_pos(self,pos):
        if pos==0:
            self.del_at_beg()
        elif pos==self.list_length():
            self.del_at_end()
        elif pos>0 and pos<self.list_length():
            idx=0
            tmp=curr=self.head
            while idx!=pos:
                tmp=curr
                curr=curr.next
                idx+=1
            tmp.next=curr.next
            curr.next.prev=tmp
        else:
            print("Invalid position!!")
        


        
        
    

n=10
cdl_list=CircularDLL()

print(f"Length of Circular double linked list is {cdl_list.list_length()}")
for i in range(10):
    cdl_list.insert_at_beg(i)
cdl_list.print_list()

for i in range(n):
    cdl_list.insert_at_end(i)
cdl_list.print_list()
print(f"Length of Circular double linked list is {cdl_list.list_length()}")
cdl_list.insert_at_pos(10,-1)
cdl_list.print_list()
k=15
print(f"index of {k} in the list is {cdl_list.get_pos_of(k)}")
print(f"Data at Index {k} is {cdl_list.get_val_at(k)}")
cdl_list.del_at_beg()
cdl_list.del_at_end()
cdl_list.print_list()
cdl_list.del_at_pos(7)
cdl_list.print_list()