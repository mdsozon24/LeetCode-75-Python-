class Solution:
    def rob(self, nums: List[int]) -> int:
        a=0
        p=0
        for n in nums:
            a,p=p,a
            a = max(a + n, p)
        return a      