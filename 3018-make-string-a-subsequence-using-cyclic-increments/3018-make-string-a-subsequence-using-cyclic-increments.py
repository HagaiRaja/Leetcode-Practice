class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def get_next_chr(ch):
            i = ord(ch) + 1
            if i == 123: i = 97
            return chr(i)
        
        i, j = 0, 0

        while i < len(str1):
            if str1[i] == str2[j] or get_next_chr(str1[i]) == str2[j]:
                j += 1
                if j == len(str2): return True
            i += 1
        return False