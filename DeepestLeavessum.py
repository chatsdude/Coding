'''Given a binary tree, return the sum of values of its deepest leave'''
def deepestLeavesSum(self, root: TreeNode) -> int:
        self.search(root, 0)
        return self.sum
    def __init__(self):
        self.deep = float('-inf')
        self.sum = 0
        
    def search(self, node, level):
        if not node:
            return
        if level > self.deep:
            self.sum = node.val
            self.deep = level
        elif level == self.deep:
            self.sum += node.val
            
        self.search(node.left, level + 1)
        self.search(node.right, level + 1)