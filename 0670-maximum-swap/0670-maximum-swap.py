class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [c for c in str(num)]
        stack = [[int(digits[0]), 0, 0]]
        for i in range(1, len(digits)):
            cur = int(digits[i])
            cur_dst = i
            while len(stack):
                val, src, dst = stack.pop()
                if val > cur:
                    stack.append([val, src, dst])
                    stack.append([cur, i, cur_dst])
                    break
                elif val < cur:
                    cur_dst = dst
                    if len(stack) == 0: # the last
                        stack.append([cur, i, cur_dst])
                        break
                else: # val == cur
                    if src == dst:
                        stack.append([val, src, dst])
                        if cur_dst != i:
                            stack.append([cur, i, cur_dst])
                    else:
                        cur_dst = dst
                        stack.append([cur, i, cur_dst])
                    break
        
        for i in range(len(stack)):
            if stack[i][1] != stack[i][2]:
                break
        
        if i == len(stack): return num
        digits[stack[i][1]], digits[stack[i][2]] = digits[stack[i][2]], digits[stack[i][1]]
        return int("".join(digits))
