# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        stack=[]
        while curr:
            stack.append(curr)
            curr=curr.next
        curr=stack.pop()
        maximum=curr.val
        result=ListNode(maximum)
        while stack:
            curr=stack.pop()
            if curr.val<maximum:
                continue
            else:
                new_node=ListNode(curr.val)
                new_node.next=result
                result=new_node
                maximum=curr.val
        return result 

            



        