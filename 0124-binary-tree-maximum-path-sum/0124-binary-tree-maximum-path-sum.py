# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.maxi=float('-inf')
        def solve(node):
            if node==None:
                return 0
            lsum=solve(node.left)
            rsum=solve(node.right)
            if lsum<0:
                lsum=0
            if rsum<0:
                rsum=0
            self.maxi=max(self.maxi,lsum+node.val+rsum)
            return node.val+max(lsum,rsum)
        solve(root)
        return self.maxi