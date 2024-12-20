# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deserialize = []
        queue = deque([root])
        while len(queue):
            cur_li = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                cur_li.append(cur)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            deserialize.append(cur_li)

        for lvl in range(1, len(deserialize)):
            if lvl & 1:
                for idx, node in enumerate(deserialize[lvl-1]):
                    node.left = deserialize[lvl][-1-(idx*2)]
                    node.right = deserialize[lvl][-2-(idx*2)]
            else:
                for idx, node in enumerate(reversed(deserialize[lvl-1])):
                    node.left = deserialize[lvl][idx*2]
                    node.right = deserialize[lvl][idx*2+1]
        
        return root