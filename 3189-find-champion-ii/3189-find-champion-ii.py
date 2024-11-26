class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        weaks = set()
        for a, b in edges:
            weaks.add(b)
        
        champ = -1
        for i in range(n):
            if i not in weaks:
                if champ == -1:
                    champ = i
                else:
                    return -1
        return champ