#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 18:02:54 2021

@author: mdshadanaltmash
"""

class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def print_likedList(self):
        curr=self.head 
        if curr is None:
            print("LinkedList is empty!!")
        else:
            while curr:
                print(curr.data,end=' ')
                curr=curr.next
                if curr==self.head:
                    break
            print('\n')
                
    def length_llist(self):
        count=1
        if self.head is None:
            return count
        else:
            curr=self.head 
            while curr.next!=self.head:
                count+=1
                curr=curr.next 
            return count
        
    def insert_at_beg(self,data):
        data=Node(data)
        data.next=self.head

        if self.head is None:
            self.head=data
            data.next=self.head
            
        else:
            curr=self.head 
            while curr.next!=self.head:
                curr=curr.next 
            curr.next=data
            self.head=data
            
    def insert_at_end(self,data):
        data=Node(data)
        if self.head is None:
            self.head=data
            data.next=self.head 
        else:
            curr=self.head 
            while curr.next != self.head:
                curr=curr.next 
            curr.next=data
            data.next=self.head 
            
    def insert_at_index(self,idx,data):
        if idx==0:
            self.insert_at_beg(data)
        elif idx==self.length_llist()-1:
            self.insert_at_end(data)
        elif idx>0 and idx<self.length_llist():
            data=Node(data)
            count=0
            curr=self.head
            while count<idx-1:
                count+=1
                curr=curr.next 
            data.next=curr.next 
            curr.next=data
        else:
            print("Invalid Index")
    def del_at_beg(self):
        if self.head is None:
            print("Circular Linked List is empty!!")
        elif self.head==self.head.next :
            self.head=None
        else:
            tmp=self.head
            curr=self.head
            while curr.next!=self.head:
                curr=curr.next
            self.head=tmp.next
            curr.next=self.head
    def del_at_end(self):
        if self.head is None:
            print("Circular Linked List is empty!!")
        elif self.head==self.head.next:
            self.head=None
        else:
            curr=self.head 
            tmp=curr
            while curr.next!=self.head:
                tmp=curr
                curr=curr.next
            tmp.next=self.head 
            
    def del_at_pos(self,idx):
        if idx==0:
            self.del_at_beg()
        elif idx==self.length_llist()-1:
            self.del_at_end()
        elif idx>0 and idx<self.length_llist():
            count=0
            curr=self.head
            tmp=curr
            while count<idx:
                count+=1
                tmp=curr
                curr=curr.next 
            tmp.next=curr.next 
        else:
            print("Invalid Index")
    def get_index_node(self,data):
        if self.head is None:
            return None
        else:
            idx=0
            curr=self.head
            if curr.data==data:
                return 0
            while curr:
                if curr.data==data:
                    return idx
                elif curr.next==self.head:
                    break
                curr=curr.next 
                idx+=1
            else:
                return -1
            
    
            


cLList=CircularLinkedList()
cLList.print_likedList()
for i in range(0,10):
    cLList.insert_at_end(i)
#cLList.del_at_beg()
#cLList.del_at_end()
cLList.print_likedList()
print("Length of Circular Linked List is ",cLList.length_llist())
cLList.insert_at_index(5,12)
#cLList.del_at_pos(4)
cLList.insert_at_index(3, 10)
cLList.insert_at_beg(11)
cLList.print_likedList()
print("Index of given node is ",cLList.get_index_node(8))
print("Length of Circular Linked List is ",cLList.length_llist())
        
    