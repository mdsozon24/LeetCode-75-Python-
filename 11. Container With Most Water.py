class Solution:
    def maxArea(self, height: List[int]) -> int:
        m=0
        i=0
        j=len(height)-1
        while i<j:
            x = min(height[i],height[j])
            a = ((j-i)*x)
            m = max(a,m)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return m