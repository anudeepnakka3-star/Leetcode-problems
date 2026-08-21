# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=0
        temp=head
        if not head or head.next is None:
            return head
        while temp is not None:
            temp=temp.next
            n+=1
        k=k%n
        while k>0:
            temp=head
            curr=head
            prev=None
            while temp.next is not None:
                prev=temp
                temp=temp.next
            head=temp
            temp.next=curr
            prev.next=None
            
            k-=1
        return head

        
        