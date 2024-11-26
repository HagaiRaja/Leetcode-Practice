class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        cnt = [0]*25
        for cand in candidates:
            i = 0
            while (cand):
                if cand & 1:
                    cnt[i] += 1
                i += 1
                cand >>= 1
        return max(cnt)