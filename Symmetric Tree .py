# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        return self.checkEqual(root.left, root.right)
    
    def checkEqual(self, n1, n2):
        if n1 == n2 == None:
            return True
        elif not n1 or not n2:
            return False
        
        if n1.val != n2.val:
            return False
        left = self.checkEqual(n1.left, n2.right)
        right = self.checkEqual(n1.right, n2.left)
        if left and right:
            return True
        else:
            return False