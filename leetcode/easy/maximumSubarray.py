from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            # i-1의 수가 0보다 크면
            if nums[i-1] > 0: 
                nums[i] += nums[i-1] # i번째 수와 i-1의 수를 더해서 최댓값을 찾는다.
            i += 1
        return max(nums)
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(Solution().maxSubArray([1])) # 1
print(Solution().maxSubArray([5,4,-1,7,8])) # 23