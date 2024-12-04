class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        next_ch = {}
        for i in range(97, 122):
            next_ch[chr(i)] = chr(i+1)
        next_ch['z'] = 'a'
        
        i, j = 0, 0

        while i < len(str1):
            if str1[i] == str2[j] or next_ch[str1[i]] == str2[j]:
                j += 1
                if j == len(str2): return True
            i += 1
        return False