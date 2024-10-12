class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        N = len(digits)
        buttons = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        combi = []
        cur_str = []
        def backtrack(i):
            if i == N:
                combi.append("".join(cur_str))
                return
            for c in buttons[digits[i]]:
                cur_str.append(c)
                backtrack(i+1)
                cur_str.pop()
                
        backtrack(0)    
        return combi