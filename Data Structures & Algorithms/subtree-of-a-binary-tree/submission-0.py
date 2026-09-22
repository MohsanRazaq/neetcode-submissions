# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def serialization(self,node:Optional[TreeNode]):
        if not node:
            return '#'
        return f",{node.val},{self.serialization(node.left)},{self.serialization(node.right)}"

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:


        return  self.serialization(subRoot) in self.serialization(root)
# time complexity , O(n)