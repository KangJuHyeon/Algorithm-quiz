# 수도코드(1)
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        # answer = nums.index(target)
        for i in range(len(nums)):
            if nums[i] < target:
                if target not in nums:
                    nums.insert(target-1, target)
                    print(nums)

            if target == 0 and target not in nums:
                nums.insert(0, 0)
                print(nums)

        answer = nums.index(target)
        print("hello", answer)
        return answer
print(Solution().searchInsert([1,3,5,6], 5)) # 2
print(Solution().searchInsert([1,3,5,6], 2)) # 1
print(Solution().searchInsert([1,3,5,6], 7)) # 4
print(Solution().searchInsert([1,3,5,6], 0)) # TestCase
print(Solution().searchInsert([1,3,5], 4))   # TestCase

# 문제풀이(1)
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)
print(Solution().searchInsert([1,3,5,6], 5)) # 2

# 문제풀이(2)
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            temp = 0
            for i in nums:
                if i > target:
                    return temp
                temp += 1
            return len(nums)
print(Solution().searchInsert([1,3,5,6], 5)) # 2