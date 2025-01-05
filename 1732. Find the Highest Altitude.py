class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pre_sum = 0
        gain = [0] + gain
        for i in range(len(gain)):
            pre_sum+=gain[i]
            gain[i] = pre_sum
        return max(gain)