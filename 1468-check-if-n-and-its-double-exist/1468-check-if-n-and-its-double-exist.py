class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        count0 = sum([0 if a else 1 for a in arr])
        if count0 > 1: return True
        arr = set(arr)
        if count0: arr.remove(0)
        for c in arr:
            if c*2 in arr:
                return True
        return False