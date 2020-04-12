class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.depthTree(root)
        return self.res

    def depthTree(self, node):
        if not node:
            return 0
        ldep = self.depthTree(node.left)
        rdep = self.depthTree(node.right)
        self.res = max(self.res, ldep+rdep)
        return max(ldep, rdep) + 1

'''
Another solution:

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        #calcolo il massimo fra diametro a destra e diametro a sinistra
        maxdiam = max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        #e ritorno il max fra diametro ed (altezza a sinistra + altezza a destra)
        return max(maxdiam, (self.height(root.left)+self.height(root.right)))

    def height(self, node: TreeNode) -> int:
        if not node:
            return 0
        return 1 + max(self.height(node.left),self.height(node.right))
'''
