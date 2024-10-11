# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        rightFirst = False
        li, ans = [root], []
        while li:
            ne = []
            val = []
            for cur in li:
                if cur.right: ne.append(cur.right)
                if cur.left: ne.append(cur.left)
                val.append(cur.val)
            if rightFirst: ans.append(val)
            else: ans.append(val[::-1])
            rightFirst = not rightFirst
            li = ne
        return ans