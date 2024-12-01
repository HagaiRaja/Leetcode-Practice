class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr = Counter(arr)
        if arr[0] > 1: return True
        del arr[0]
        for c in arr:
            if c*2 in arr:
                return True
        return False