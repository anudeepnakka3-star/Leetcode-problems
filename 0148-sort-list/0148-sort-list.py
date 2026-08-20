# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val=[]
        temp=head
        while temp is not None:
            val.append(temp.val)
            temp=temp.next
        temp=head
        val.sort()
        i=0
        while temp is not None:
            temp.val=val[i]
            i+=1
            temp=temp.next
        return head
        