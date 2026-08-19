# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            temp=head
            prev=None
            while temp is not None:
                front=temp.next
                temp.next=prev
                prev=temp
                temp=front
            return prev
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        rev=reverse(slow)
        while rev:
            if head.val!=rev.val:
                return False
            rev=rev.next
            head=head.next
        return True

        