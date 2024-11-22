class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = defaultdict(int)
        for row in matrix:
            real, flip = "", ""
            for val in row:
                real += str(val)
                if val == 1: flip += "0"
                else: flip += "1"
            cnt[real] += 1
            cnt[flip] += 1
        ans = 1
        for val in cnt:
            ans = max(ans, cnt[val])
        return ans