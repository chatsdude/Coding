class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        d={}
        for i,j in enumerate(inorder):
            d[j]=i
        def helper(left,right):
            if left>right:
                return 
            root=TreeNode(postorder.pop())
            index=d[root.val]
            root.right=helper(index+1,right)
            root.left=helper(left,index-1)
            return root
        return helper(0,len(inorder)-1)
        
