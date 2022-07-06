# Memoization 이용 재귀
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return n
        stp = [0, 1, 2] + [-1] * (n-2)
        return self.recur(n, stp)
        
    def recur(self, n, stp):
        if stp[n] == -1:
            stp[n]=self.recur(n-1, stp)+self.recur(n-2, stp)
        return stp[n]
print(Solution().climbStairs(2))