class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        cur = m+n - 1
        while (True):
            if (j == -1):
                break
            if (i == -1):
                nums1[cur] = nums2[j]
                j -= 1
                cur -= 1
                continue
            
            if (nums1[i] < nums2[j]):
                nums1[cur] = nums2[j]
                j -= 1
            else:
                nums1[cur] = nums1[i]
                i -= 1
            cur -= 1