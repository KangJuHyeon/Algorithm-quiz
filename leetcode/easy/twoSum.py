# 문제풀이
# List에 담아서 sum() 함수 사용
# 하나씩 넣고 target과 같다면, 조건문을 썼다. 안일했다.
# 앞뒤를 비교하기 시작, for문 하나만 쓰면 [3,3]에서 똑같은 인덱스라고 인식해서 실패
# 이중포문으로 리스트에 앞뒤를 비교해야 [3,3] 똑같은 값으로 인식을 안한다. [0,1]이라는 값 출력

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                print(i, j)
                result = nums[i] + nums[j]
                print(result)
                if result == target:
                    return [i, j]

# nums = [3, 2, 4]
# target = 6
# Output: [1, 2]

print(Solution().twoSum([3, 2, 4], 6))