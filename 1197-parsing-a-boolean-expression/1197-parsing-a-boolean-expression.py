class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def parseAnd(j):
            i = j
            ans = True
            while expression[i] != ")":
                if expression[i] == "&":
                    res, i = parseAnd(i+2)
                    ans &= res
                elif expression[i] == "|":
                    res, i = parseOr(i+2)
                    ans &= res
                elif expression[i] == "!":
                    res, i = parseNot(i+2)
                    ans &= res
                elif expression[i] == "f":
                    ans = False
                    if expression[i+1] == ",":
                        i += 2
                    else:
                        i += 1
                elif expression[i] == "t":
                    if expression[i+1] == ",":
                        i += 2
                    else:
                        i += 1
                elif expression[i] == ",":
                    i += 1
                
            return ans, i+1

        def parseOr(j):
            i = j
            ans = False
            while expression[i] != ")":
                if expression[i] == "&":
                    res, i = parseAnd(i+2)
                    ans |= res
                elif expression[i] == "|":
                    res, i = parseOr(i+2)
                    ans |= res
                elif expression[i] == "!":
                    res, i = parseNot(i+2)
                    ans |= res
                elif expression[i] == "f":
                    if expression[i+1] == ",":
                        i += 2
                    else:
                        i += 1
                elif expression[i] == "t":
                    ans = True
                    if expression[i+1] == ",":
                        i += 2
                    else:
                        i += 1
                elif expression[i] == ",":
                    i += 1
                
            return ans, i+1

        def parseNot(i):
            if expression[i] == "&":
                res, i = parseAnd(i+2)
                return not res, i+1
            elif expression[i] == "|":
                res, i = parseOr(i+2)
                return not res, i+1
            elif expression[i] == "!":
                res, i = parseNot(i+2)
                return not res, i+1
            elif expression[i] == "f":
                return True, i+2
            elif expression[i] == "t":
                return False, i+2
        
        if expression[0] == "f": return False
        elif expression[0] == "t": return True
        elif expression[0] == "&":
            res, i = parseAnd(2)
            return res
        elif expression[0] == "|": 
            res, i = parseOr(2)
            return res
        elif expression[0] == "!": 
            res, i = parseNot(2)
            return res