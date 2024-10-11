"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # bfs
        if root == None: return None
        li = [root]
        while len(li):
            ne = []
            for i in range(len(li)-1):
                if li[i].left: ne.append(li[i].left)
                if li[i].right: ne.append(li[i].right)
                li[i].next = li[i+1]
            if li[-1].left: ne.append(li[-1].left)
            if li[-1].right: ne.append(li[-1].right)
            li[-1].next = None
            li = ne
        return root