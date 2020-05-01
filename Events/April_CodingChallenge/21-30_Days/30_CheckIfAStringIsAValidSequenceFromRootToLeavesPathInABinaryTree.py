# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        self.sol = False

        def rec(node,path):
            if not path:
                if not node.left and not node.right:
                    self.sol = True
                return
            if node.left and node.left.val == path[0]:
                rec(node.left,path[1:])
            if node.right and node.right.val == path[0]:
                rec(node.right,path[1:])

        if root.val==arr[0]: rec(root,arr[1:])
        return self.sol
