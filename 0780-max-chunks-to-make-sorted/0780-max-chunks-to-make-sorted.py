class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        temp = [[arr[0]]]
        ans = [1]
        def eval():
            i = 0
            for chunk in temp:
                minn, maxx = min(chunk), max(chunk)
                if min(chunk) == i and max(chunk) == (i+len(chunk)-1):
                    i = maxx + 1
                else: return
            ans[0] = max(ans[0], len(temp))

        def backtrack(i):
            if i == len(arr):
                eval()
                return
            # append chunk
            temp[-1].append(arr[i])
            backtrack(i+1)
            temp[-1].pop()
            # new chunks
            temp.append([arr[i]])
            backtrack(i+1)
            temp.pop()
        
        backtrack(1)
        return ans[0]
            

