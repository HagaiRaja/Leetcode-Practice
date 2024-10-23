# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([[root, root]])

        while len(queue):
            cnt = defaultdict(int)
            sums = 0
            for i in range(len(queue)):
                cur, parent = queue.popleft()
                cnt[parent] += cur.val
                sums += cur.val
                queue.append([cur, parent])

            for _ in range(len(queue)):
                cur, parent = queue.popleft()
                cur.val = sums - cnt[parent]
                if cur.left: queue.append([cur.left, cur])
                if cur.right: queue.append([cur.right, cur])
        return root
                