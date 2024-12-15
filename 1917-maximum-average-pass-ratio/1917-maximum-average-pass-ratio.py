class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def calc_prio(p, t):
            return ((p+1)/(t+1)) - (p/t)

        prio = []
        for i in range(len(classes)):
            entry = [-calc_prio(classes[i][0], classes[i][1]), i]
            prio.append(entry)
        
        heapq.heapify(prio)
        for _ in range(extraStudents):
            _, i = heapq.heappop(prio)
            classes[i][0] += 1
            classes[i][1] += 1
            new_entry = [-calc_prio(classes[i][0], classes[i][1]), i]
            heapq.heappush(prio, new_entry)
        
        avg_pass = []
        for i in range(len(classes)):
            avg_pass.append(classes[i][0]/classes[i][1])
        return sum(avg_pass)/len(avg_pass)