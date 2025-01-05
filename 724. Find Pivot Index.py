class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            if left == (right-left-nums[i]):
                return i
            left+=nums[i]
        return -1