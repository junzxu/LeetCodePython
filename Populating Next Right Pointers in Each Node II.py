# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left and node.right:
                node.left.next = node.right
                next = self.search(node)
                if next:
                    if next.left:
                        node.right.next = next.left
                    elif next.right:
                        node.right.next = next.right
                queue.append(node.left)
                queue.append(node.right)
                
            elif node.left and not node.right:
                next = self.search(node)
                if next:
                    if next.left:
                        node.left.next = next.left
                    elif next.right:
                        node.left.next = next.right
                queue.append(node.left)
                
            elif node.right and not node.left:
                next = self.search(node)
                if next:
                    if next.left:
                        node.right.next = next.left
                    elif next.right:
                        node.right.next = next.right
                queue.append(node.right)
                
    
    def search(self, node):
        #search for the next node that has child node in the same level
        next = node.next
        while next:
            if next.left or next.right:
                return next
            else:
                next = next.next
        return None