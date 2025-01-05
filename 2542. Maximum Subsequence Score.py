class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pair = [(n1,n2) for n1,n2 in zip(nums1,nums2)]
        pair = sorted(pair,key = lambda p:p[1],reverse= True)
        ans = 0
        sm = 0
        hp = []
        for n1,n2 in pair:
            sm+=n1
            heapq.heappush(hp,n1)
            if len(hp) > k:
                val = heapq.heappop(hp)
                sm-=val
            if len(hp)==k:
                ans = max(ans,sm*n2)
        return ans