from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        answer = []
        for num in nums:
            print("num", num)
            print("힝구", nums.count(num))
            while nums.count(num) > 1:
                print("hello", nums.count(num)) 
                nums.remove(num)
                print("result", nums)
        return len(nums)
print(Solution().removeDuplicates([1,1,2])) # [1,2,_]
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # [0,1,2,3,4,_,_,_,_,_]

# 결과 값
# 입력: 숫자 = [1,1,2]
# 출력: 2, 숫자 = [1,2,_]
# 설명: 함수는 k = 2를 반환해야 하며 nums의 처음 두 요소는 각각 1과 2입니다.
# 반환된 k(따라서 밑줄임) 뒤에 무엇을 남겨두어도 상관 없습니다.

# 입력: 숫자 = [0,0,1,1,1,2,2,3,3,4]
# 출력: 5, 숫자 = [0,1,2,3,4,_,_,_,_,_]
# 설명: 함수는 k = 5를 반환해야 하며 nums의 처음 5개 요소는 각각 0, 1, 2, 3, 4입니다.
# 반환된 k(따라서 밑줄임) 뒤에 무엇을 남겨두어도 상관 없습니다.