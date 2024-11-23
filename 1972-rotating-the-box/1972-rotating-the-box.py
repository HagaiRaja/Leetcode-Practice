class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        ans = [["."]*m for _ in range(n)]
        for i in range(m):
            newRow = []
            dot, leaf = 0, 0
            for val in reversed(box[i]):
                if val == ".":
                    dot += 1
                elif val == "#":
                    leaf += 1
                else:
                    last = (["#"]*leaf) + (["."]*dot) + ["*"]
                    newRow += last
                    dot, leaf = 0, 0
            newRow += (["#"]*leaf) + (["."]*dot)
            for j in range(n):
                ans[n-1-j][m-1-i] = newRow[j]

        return ans