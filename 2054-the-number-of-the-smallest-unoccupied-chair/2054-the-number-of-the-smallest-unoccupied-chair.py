class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_arrival = times[targetFriend][0]
        times.sort()

        chair_num, occ_chair, unocc_chair = 0, [], []
        heapq.heapify(occ_chair)
        heapq.heapify(unocc_chair)

        for arr, lea in times:
            # free the occ_chair
            while len(occ_chair):
                cur_lea, cur_chair, cur_arr = heapq.heappop(occ_chair)
                if cur_lea > arr:
                    heapq.heappush(occ_chair, [cur_lea, cur_chair, cur_arr])
                    break
                heappush(unocc_chair, cur_chair)

            # get unocc_chair
            if len(unocc_chair):
                chair = heapq.heappop(unocc_chair)
            else:
                chair = chair_num
                chair_num += 1
            if arr == target_arrival: return chair
            heapq.heappush(occ_chair, [lea, chair, arr])