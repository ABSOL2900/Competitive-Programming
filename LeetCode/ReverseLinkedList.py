# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        
        head2=None
        while temp:
            dummy=ListNode(temp.val,head2)
            head2=dummy
            temp=temp.next
        return head2

        


        
            