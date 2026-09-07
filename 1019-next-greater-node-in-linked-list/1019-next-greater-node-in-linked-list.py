# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        temp=head
        prev=None
        n=0
        while temp:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
            n+=1
        temp=prev
        stack=[]
        ans=[0]*n
        l=0
        while temp is not None:
            while stack and stack[-1]<=temp.val:
                stack.pop()
            if len(stack)!=0 and l<n:
                ans[l]=stack[-1]
                
            stack.append(temp.val)
            l+=1
            temp=temp.next
        
       
        return ans[::-1]

        