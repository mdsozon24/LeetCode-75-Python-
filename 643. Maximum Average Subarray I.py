class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = 0
        window = 0
        for i in range(k):
            window+=nums[i]
        res = window/k
        for i in range(k,len(nums)):
            window+=nums[i]
            window-=nums[i-k]
            res = max(res,window/k)
        return res