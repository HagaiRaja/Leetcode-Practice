# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        last_cor = None
        cur = head
        while cur:
            ne = cur.next
            if ne and (ne.val == cur.val):
                # don't include
                while ne and (ne.val == cur.val):
                    ne = ne.next
            else:
                # include
                if ans == None:
                    ans = cur
                    last_cor = ans
                else:
                    last_cor.next = cur
                    last_cor = cur
            cur = ne
        if last_cor: last_cor.next = None
        return ans