class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i,j=0,len(nums)-1
        res = 0
        nums = sorted(nums)
        while i<j:
            if nums[i]+nums[j]<k:
                i+=1
            elif nums[i]+nums[j]>k:
                j-=1
            else:
                res+=1
                i+=1
                j-=1
        return res