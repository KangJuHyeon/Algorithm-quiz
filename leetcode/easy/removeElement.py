# 문제 접근
# in-place 알고리즘을 사용하라는 것인지? 퀵 정렬, 삽입 정렬 등등
# val이 2만 제거하는 것인지?
# 중복 제거를 해야되는지?
# 삭제를 진행할 수도 있다.

# 문제풀이(1)
from typing import List

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        answer = []

        for num in nums:
            print("num", num)
            if num != val:
                answer.append(num)
            print("answer", answer)
        print("len(answer)", len(answer))

        for i in range(len(answer)):
            nums[i] = answer[i]
        print("nums[i]", nums[i])
        
        nums = nums[:len(answer)]
        print("nums", nums)

        return len(nums)
print(Solution().removeElement([3,2,2,3], 3))
print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))

# 문제풀이(2)
from typing import List

class Solution2:
    def removeElement(self, nums: list[int], val: int) -> int:
        while nums.count(val):
            nums.remove(val)
        print(nums)
        return len(nums)
print(Solution2().removeElement([3,2,2,3], 3))
print(Solution2().removeElement([0,1,2,2,3,0,4,2], 2))