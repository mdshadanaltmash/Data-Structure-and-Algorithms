"""
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.

Input: head = [0,3,1,0,4,5,2,0]
Output: [4,11]
Explanation: 
The above figure represents the given linked list. The modified list contains
- The sum of the nodes marked in green: 3 + 1 = 4.
- The sum of the nodes marked in red: 4 + 5 + 2 = 11.
"""

from SinglyLinkedList import Node, SingleLinkedList

def mergeNodes( self):
    tmp = self.head.next
    self.head=self.head.next
    while self.head:
        tmpVal=self.head.data
        tmpNode = self.head.next
        while tmpNode.data!=0:
            tmpVal+=tmpNode.data
            tmpNode=tmpNode.next
        self.head.data=tmpVal
        self.head.next=tmpNode.next
        self.head=self.head.next
    return tmp

a=[0,1,1,2,5,0,2,0,3,4,7,0,5,5,6,0]
llist=SingleLinkedList()
for i in a:
    llist.insert_at_end(i)
result = mergeNodes(llist)
llist.print_likedList()
while result:
    print(result.data, end='-->')
    result=result.next