class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        hep_left = costs[:candidates]
        hep_right = costs[max(candidates,n-candidates):]
        ans = 0
        heapify(hep_left)
        heapify(hep_right)
        left,right = candidates,n-candidates-1

        for _ in range(k):
            if not hep_right or (hep_left and (hep_left[0]<=hep_right[0])):
                ans+=heapq.heappop(hep_left)
                if left<=right:
                    heapq.heappush(hep_left,costs[left])
                    left+=1
            else:
                ans+=heapq.heappop(hep_right)
                if left<=right:
                    heapq.heappush(hep_right,costs[right])
                    right-=1

        return ans