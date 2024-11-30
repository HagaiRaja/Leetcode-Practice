class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph, ins, out = defaultdict(list), defaultdict(int), defaultdict(int)
        for start, end in pairs:
            graph[start].append(end)
            ins[start] += 1
            out[end] += 1

        # need to be the start
        start = -1
        for s in ins:
            if s not in out or ins[s] > out[s]:
                start = s
                break

        if start == -1:
            start = pairs[0][0]

        result = []
        nodeStack = [start]
        while nodeStack:
            node = nodeStack[-1]
            if graph[node]:
                nextNode = graph[node].pop(0)
                nodeStack.append(nextNode)
            else:
                result.append(node)
                nodeStack.pop()
        
        result.reverse()

        pairedResult = []
        for i in range(len(result)-1):
            pairedResult.append([result[i], result[i+1]])
        return pairedResult