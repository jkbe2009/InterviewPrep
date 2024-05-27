
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        """
        preorder = [3,9,20,15,7], 
        inorder = [9,3,15,20,7]
        """
        
        # Base case:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        m = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:m+1], inorder[:m])
        root.right = self.buildTree(preorder[m+1:], inorder[m+1:])

        return root

        