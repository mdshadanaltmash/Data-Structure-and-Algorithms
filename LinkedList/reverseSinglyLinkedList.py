from SinglyLinkedList import SingleLinkedList, print_linkedlist
def reverseLinkedList(self):
    curr = self.head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

a=[1,1,1,2,2,3,4,5,5,6]
llist=SingleLinkedList()
for i in a:
    llist.insert_at_end(i)
llist.print_likedList()
rllist =reverseLinkedList(llist)
print_linkedlist(rllist)