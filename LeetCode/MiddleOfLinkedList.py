# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp=head
        num=0
        while temp:
            num+=1
            temp=temp.next
        middle=math.ceil(num/2)
        if num%2==0:
            middle=middle+1
        i=1
        while i<middle:
            head=head.next
            i+=1
        return head
            