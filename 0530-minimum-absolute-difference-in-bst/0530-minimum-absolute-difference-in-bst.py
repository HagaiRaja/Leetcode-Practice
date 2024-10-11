# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def flatten(cur):
            if cur == None: return []
            return flatten(cur.left) + [cur.val] + flatten(cur.right)
        flat = flatten(root)
        ans = 1e6
        for i in range(1, len(flat)):
            ans = min(ans, flat[i]-flat[i-1])
        return ans