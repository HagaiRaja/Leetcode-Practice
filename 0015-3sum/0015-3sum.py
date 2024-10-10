class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # filtering first
        tab = dict()
        for n in nums:
            if (n not in tab):
                tab[n] = 0
            tab[n] += 1
        nums = []
        for t in tab:
            i = 0
            while (i < 3 and i < tab[t]):
                nums.append(t)
                i += 1
        
        n = len(nums)
        nums = sorted(nums)
        ans = []
        anss = set()
        for i in range(n-2):
            for j in range(i+1,n-1):
                curr = nums[i] + nums[j]
                l = j + 1
                r = n - 1
                while (l < r):
                    mid = (l+r) // 2
                    if (nums[mid] + curr > 0):
                        r = mid - 1
                    elif (nums[mid] + curr < 0):
                        l = mid + 1
                    else:
                        l = mid
                        break
                if (nums[l] + curr == 0):
                    new_ans = [nums[i], nums[j], nums[l]]
                    # print(new_ans)
                    new_ans = sorted(new_ans)
                    key = ""
                    for news in new_ans:
                        key += str(news)
                    if (key not in anss):
                        anss.add(key)
                        ans.append(new_ans)
        return ans
        