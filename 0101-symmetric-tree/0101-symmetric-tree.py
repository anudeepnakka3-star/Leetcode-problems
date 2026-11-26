# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        lh=root.left
        rh=root.right
        def isSameTree( p: TreeNode | None, q: TreeNode | None) -> bool:
            if p==None or q==None:
                return (p==q)
            return (p.val==q.val) and (isSameTree(p.left,q.right)) and (isSameTree(p.right,q.left))
        return isSameTree(lh,rh)
        


        