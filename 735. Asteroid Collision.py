class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            while ans and a < 0 < ans[-1]:
                if abs(ans[-1]) < abs(a):
                    ans.pop()
                elif abs(ans[-1]) == abs(a):
                    ans.pop()
                    break
                else:
                    break
            else:
                ans.append(a)
        return ans
