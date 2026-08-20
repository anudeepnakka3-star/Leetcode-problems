# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        le=0
        while temp is not None:
            temp=temp.next
            le+=1
        if le==n:
            new_head=head.next
            return new_head
        node=le-n
        c=1
        temp=head
        while c<node:
            temp=temp.next
            c+=1
        temp.next=temp.next.next
        return head
            


        