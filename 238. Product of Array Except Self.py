class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        pr = 1
        for i in range(len(nums)):
            ans[i] = pr
            pr*=nums[i]
        po = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= po
            po*=nums[i]
        return ans