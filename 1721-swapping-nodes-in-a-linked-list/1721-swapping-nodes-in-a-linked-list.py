# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        arr[k-1],arr[-k]=arr[-k],arr[k-1]
        dummy=ListNode(0)
        ptr=dummy
        for i in range(len(arr)):
            new_node=ListNode(arr[i])
            ptr.next=new_node
            ptr=ptr.next
        return dummy.next



        