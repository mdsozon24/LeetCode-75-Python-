class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stk and temperatures[stk[-1]] < temperatures[i]:
                x = stk.pop()
                ans[x] = (i-x)
            stk.append(i)
        return ans