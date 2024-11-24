class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sums, min_num = 0, 10**6
        neg_cnt, is_zero = 0, False
        for row in matrix:
            for val in row:
                if val < 0:
                    neg_cnt += 1
                    val *= -1
                elif val == 0:
                    is_zero = True
                min_num = min(min_num, val)
                sums += val

        if is_zero: return sums
        if neg_cnt & 1:
            return sums - (2*min_num)
        return sums
