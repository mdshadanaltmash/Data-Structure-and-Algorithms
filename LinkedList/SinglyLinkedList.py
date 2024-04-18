#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 20:24:36 2021

@author: mdshadanaltmash
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        # self.tail=None

    def print_likedList(self):
        curr = self.head
        if curr is None:
            print("LinkedList is empty!!")
        else:
            while curr is not None:
                print(curr.data, end='-->')
                curr = curr.next
            print('\n')

    def length_llist(self):
        count = 0
        if self.head is None:
            return count
        else:
            curr = self.head
            while curr is not None:
                count += 1
                curr = curr.next
            return count

    def insert_at_beg(self, data):
        data = Node(data)
        if self.head is None:
            self.head = data
        else:
            data.next = self.head
            self.head = data

    def insert_at_end(self, data):
        data = Node(data)
        if self.head is None:
            self.head = data
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = data

    def insertNode(self, data, pos):
        data = Node(data)
        if self.head is None:
            self.head = data
        else:
            if pos == 0:
                data.next = self.head
                self.head = data
            elif pos == sLinkedList.length_llist():
                curr = self.head
                while curr.next is not None:
                    curr = curr.next
                curr.next = data
            else:
                idx = 0
                curr = self.head
                while idx < pos - 1:
                    idx += 1
                    curr = curr.next
                data.next = curr.next
                curr.next = data

    def getIndexOfNode(self, data):
        if self.head is None:
            return None
        else:
            curr = self.head
            idx = 0
            while curr is not None:
                if curr.data != data:
                    idx += 1
                    curr = curr.next
                else:
                    return idx
            else:
                return -1

    def delByIndex(self, idx):
        if self.head is None:
            print("Linked List is Empty")
        else:
            curr = self.head
            if idx == 0 and self.length_llist() == 1:
                self.head = None
            elif idx == 0 and self.length_llist() > 1:
                self.head = curr.next
                curr.next = None
            elif idx == self.length_llist() - 1:
                count = 0
                while count < idx - 1:
                    count += 1
                    curr = curr.next
                curr.next = None
            elif idx > 0 and idx < self.length_llist() - 1:
                count = 0
                while count < idx - 1:
                    count += 1
                    curr = curr.next
                tmp = curr.next
                curr.next = tmp.next
            else:
                print("Invalid Index")

    def delByData(self, data):
        if self.head is None:
            print("Linked List is Empty")
        else:
            if self.length_llist() == 1:
                if data == self.head.data:
                    self.head = None
                else:
                    print("Data is not present in the list")
            else:
                curr = self.head
                tmp = curr
                if curr.data == data:
                    self.head = curr.next
                    return

                while curr is not None:
                    if data == curr.data:
                        if curr.next is None:
                            tmp.next = None
                            return
                        else:
                            tmp.next = curr.next
                            return
                    else:
                        tmp = curr
                        curr = curr.next
                else:
                    print("Data is not present in the list")


def print_linkedlist(head):
    while head:
        print(head.data, end='-->')
        head = head.next


if __name__ == '__main__':
    sLinkedList = SingleLinkedList()

    sLinkedList.print_likedList()
    sLinkedList.insertNode(1, 0)
    # sLinkedList.delByData(1)
    sLinkedList.print_likedList()
    sLinkedList.insertNode(3, 0)
    sLinkedList.insertNode(5, 1)
    print(sLinkedList.length_llist())
    sLinkedList.delByIndex(2)

    sLinkedList.print_likedList()
    print("\nLength of Linked list is ", sLinkedList.length_llist())

    sLinkedList.insertNode(2, sLinkedList.length_llist())
    sLinkedList.print_likedList()

    print("\nLength of Linked list is ", sLinkedList.length_llist())
    sLinkedList.insertNode(4, 1)
    sLinkedList.insert_at_beg(10)
    sLinkedList.insert_at_end(11)
    sLinkedList.delByIndex(3)
    sLinkedList.delByData(111)
    sLinkedList.print_likedList()
    print("Length of Linked list is ", sLinkedList.length_llist())
    print(sLinkedList.getIndexOfNode(10))

    a = [1, 1, 1, 2, 2, 3, 4, 5, 5, 6]
    llist = SingleLinkedList()
    for i in a:
        llist.insert_at_end(i)

    sLinkedList.print_likedList()
