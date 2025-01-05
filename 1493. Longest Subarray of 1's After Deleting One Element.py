class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        x = 0
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                x += 1
            while x > 1:
                if nums[i] == 0:
                    x -= 1
                i += 1
            res = max(res, (j - i))
            j += 1
        return res