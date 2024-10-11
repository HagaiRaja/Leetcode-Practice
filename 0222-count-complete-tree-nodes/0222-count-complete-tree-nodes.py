# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0
        ans = 0
        que = [root]
        while que:
            cur = que.pop()
            ans += 1
            if cur.left: que.append(cur.left)
            if cur.right: que.append(cur.right)
        return ans