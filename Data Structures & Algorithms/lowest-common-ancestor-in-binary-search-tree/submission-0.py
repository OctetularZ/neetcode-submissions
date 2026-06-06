# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not p or not q:
            return root
        
        min_node = min(p.val, q.val)
        max_node = max(p.val, q.val)

        if min_node == root.val or max_node == root.val:
            return root

        while True: # Answer can always be found according to constraints so while True can be used (no risk of infinite loop)
            if root:
                print(root.val)
            else:
                print(root)

            if (p.val <= root.val and q.val >= root.val) or (q.val <= root.val and p.val >= root.val):
                return root
            
            if (p.val < root.val) and (q.val < root.val):
                root = root.left
            else:
                root = root.right
        
        return False

# BST tree - 
    # Everything in node.left is less than node
    # Everything in node.right is more than node

# So starting from root, if p is less than root and q is more than root, then root is the LCA
# If not search based on values
# If p and q more than root or p and q less than root, go to left or right tree accordingly
# 