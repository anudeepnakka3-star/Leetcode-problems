# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def last_node(head,c):
            temp=head
            cnt=1
            while cnt<c:
                temp=temp.next
                cnt+=1
            return temp

        if head is None or head.next is None:
            return head
        n=1
        tail=head
        while tail.next is not None:
            tail=tail.next
            n+=1
        if k==n:
            return head
        k=k%n
        tail.next=head
        new_last_node=last_node(head,n-k)
        head=new_last_node.next
        new_last_node.next=None
        return head
            

        
        