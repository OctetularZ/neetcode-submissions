# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        reached = 0
        res = root.val

        def dfs(node):
            nonlocal reached, res

            if not node:
                return

            dfs(node.left)
            if reached == k:
                return
            reached += 1
            if reached == k:
                res = node.val
                return
            dfs(node.right)
        
        dfs(root)
        return res


# Method #1 (probably something more optimal):
    # Put all node values in an array
    # Sort array
    # Get k index from array

# Method #2:
    # In-order traversal
    # Go to left-most node to get the smallest element
    # Then as we go up, we get the next smallest element
    # Repeat k times to the element
