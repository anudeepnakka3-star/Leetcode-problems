# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        result=[]
        queue=deque([])
        if root is None:
            return []
        if root is not None:
            queue.append(root)
            
        while len(queue)!=0:
            size=len(queue)
            r=[]
            for i in range(size):
                e=queue.popleft()
                if e.left is not None:
                    queue.append(e.left)
                if e.right is not None:
                    queue.append(e.right)
                r.append(e.val)
            result.append(r)
                
        return result
        
        