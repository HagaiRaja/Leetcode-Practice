# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []
        queue = deque([root])

        while len(queue):
            cur_sum = 0
            for _ in range(len(queue)):
                cur = queue.popleft()
                cur_sum += cur.val
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            sums.append(cur_sum)
        
        if len(sums) < k: return -1
        sums.sort()
        return sums[-k]