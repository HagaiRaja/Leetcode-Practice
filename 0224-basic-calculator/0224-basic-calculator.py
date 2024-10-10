class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")

        def calc_inner(idx):
            val, last_ope = 0, "+"
            buf = ""
            while idx < len(s):
                if s[idx] == "-":
                    if buf == "": buf += "-"
                    else:
                        if last_ope == "+":
                            val += int(buf)
                        else:
                            val -= int(buf)
                        last_ope = "-"
                        buf = ""
                elif s[idx] == "+":
                    if last_ope == "+":
                        val += int(buf)
                    else:
                        val -= int(buf)
                    last_ope = "+"
                    buf = ""
                elif s[idx] == "(":
                    last_val, last_idx = calc_inner(idx+1)
                    if buf == "-": buf = str(last_val*-1)
                    else: buf = str(last_val)
                    idx = last_idx
                elif s[idx] == ")":
                    if last_ope == "+":
                        val += int(buf)
                    else:
                        val -= int(buf)
                    return val, idx
                else:
                    buf += s[idx]
                idx += 1

            if buf != "":
                if last_ope == "+":
                    val += int(buf)
                else:
                    val -= int(buf)
            return val, idx

        ans, idx = calc_inner(0)
        return ans