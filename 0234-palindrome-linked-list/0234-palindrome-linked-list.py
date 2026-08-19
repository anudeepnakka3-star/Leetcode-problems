# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp=head
        val=[]
        while temp is not None:
            val.append(temp.val)
            temp=temp.next
        l=0
        r=len(val)-1
        while l<r and val[l]==val[r]:
            l+=1
            r-=1
        if l>=r:
            return True
        return False

        


        