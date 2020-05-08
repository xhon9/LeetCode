# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def depth(node,val,level,father=None):
            if not node: return
            if node.val==val: return (level,father)
            return depth(node.left,val,level+1,father=node) or depth(node.right,val,level+1,father=node)
        d1=depth(root,x,0)
        d2=depth(root,y,0)
        return d1[0]==d2[0] and d1[1]!=d2[1]
