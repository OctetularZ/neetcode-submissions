# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        goodNodes = 0

        def dfs(node, max_node):
            nonlocal goodNodes
            if not node:
                return
            
            if node.val >= max_node:
                goodNodes += 1
            
            max_node = max(max_node, node.val)

            dfs(node.left, max_node)
            dfs(node.right, max_node)

            return


        dfs(root, float('-inf'))
        return goodNodes
        

# Hold current maximum node as we traverse down tree (dfs)
# Complete search for each node in the tree
# Root node is always a good node as there is nothing before it, so we always at least return 1
# At each node, check if max is greater than current node, if not, then current node is a good node.