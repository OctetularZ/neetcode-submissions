# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree = []

        def dfs(node):
            nonlocal tree

            if not node:
                tree.append(None)
                return
            
            tree.append(node.val)
            dfs(node.left)
            dfs(node.right)

            return
        
        dfs(p)
        tree1 = tree[:]
        tree = []
        dfs(q)
        tree2 = tree[:]
        return tree1 == tree2