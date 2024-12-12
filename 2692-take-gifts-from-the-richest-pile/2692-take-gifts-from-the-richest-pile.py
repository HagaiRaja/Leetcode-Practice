class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            maxi = 0
            for i in range(1, len(gifts)):
                if gifts[i] > gifts[maxi]:
                    maxi = i
            gifts[maxi] = int(gifts[maxi]**0.5)
        return sum(gifts)