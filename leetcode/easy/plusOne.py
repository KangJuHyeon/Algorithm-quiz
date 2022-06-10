from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_1 = "".join(map(str, digits))
        num_2 = 1

        for i in range(len(digits)):
            answer = int(num_1) + num_2
            print("num", answer)
            
        return list(str(answer))

print(Solution().plusOne([1,2,3])) # [1,2,4]
print(Solution().plusOne([4,3,2,1])) # [4,3,2,2]
print(Solution().plusOne([9])) # [1,0]