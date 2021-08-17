# 문제 풀이
# N마리 폰켓몬의 종류 번호가 담긴 배열 nums가 매개변수로 주어지고,
# N/2 마리의 폰켓몬을 선택하는 방법 중 가장 많은 종류의 폰켓몬을 선택하는 방법을 찾고,
# 그 때의 폰켓몬 종류 번호의 개수를 리턴하라. 
# [3, 1, 2, 3] => return 2
# [3, 3, 3, 2, 2, 4] => return 3
# [3, 3, 3, 2, 2, 2] => return 2 

# 입출력 예시 3번
# 6마리의 폰켓몬이 있으므로, 3마리의 폰켓몬을 골라야 합니다.
# 가장 많은 종류의 폰켓몬을 고르기 위해서는 3번 폰켓몬 한 마리와 2번 폰켓몬 두 마리를 고르거나, 혹은 3번 폰켓몬 두 마리와 2번 폰켓몬 한 마리를 고르면 됩니다. 
# 따라서 최대 고를 수 있는 폰켓몬 종류의 수는 2입니다.

# 문제 접근
# [3,1,2,3] => 4마리 중 2마리를 선정하는데 다양한 종류를 카운트 => 2 
# [3,3,3,2,2,4] => 6마리 중 3마리를 선정하는데 다양한 종류를 카운트 => 3
# [3,3,3,2,2,2] => 6마리 중 3마리를 선정하는데 같은 종류의 최댓값은 2로 정한다. [2,2,3] => 2, [3,3,2] => 2
# 중복제거? 배열을 하나 생성해서 비교연산이 더 좋을 것 같다.
# 생각보다 잘 안풀린다. 카운팅 개념으로 생각하는데 아닌 것 같고, if [0] != [i]가 다를 때 종류 번호를 세면 안될 것 같다.
# 중복 제거를 했을 때

# 수도코드(1)
nums = [3,1,2,3]
# [3,1,2,3], [3,3,3,2,2,4], [3,3,3,2,2,2]
arr = []
answer = int(len(nums)/2) # 4/2 = 2, 6/2 = 3, 6/2 = 3
for num in nums: # [3,1,2,3] => num = 3, 1, 2, 3
    if num not in arr: # [] 안에 num값이 포함되어 있지 않다면
        arr.append(num) # num의 값을 []배열안에 추가시켜준다. => [3], [3, 1], [3, 1, 2] || [3], [3, 2], [3, 2, 4] || [3], [3, 2]
        # print(len(arr))
    if answer > len(arr): # 만약에 2 > 3 라면, 만약 3 > 3 라면(2, 3조건 불충족)
        result = len(arr) # 3
    else: # 그게 아니라면 2, 3조건 충족
        print(answer) # 2, 3
print(result)

# 문제풀이(1)
def solution(nums):
    arr = []
    answer = len(nums) / 2
    for num in nums:
        if num not in arr:
            arr.append(num)
        if answer > len(arr):
            result = len(arr)
        else:
            return answer
    return result

# 수도코드(2)
nums = [3,1,2,3]
# [3,1,2,3], [3,3,3,2,2,4], [3,3,3,2,2,2]
answer = 0
result = len(nums) / 2 # 6/2 = 3, 4/2 = 2
nums = list(set(nums)) # [3,2,4]
if len(nums) >= result: # 3 >= 3, 2 >= 3
    answer = result     # 0 = 3,  0 = 3
elif len(nums) < result: # 3 < 3, 2 < 3
    answer = len(nums) # 0 = 3, 0 = 2
print(answer)

# line 45 : nums의 길이 반이 고를 수 있는 폰켓몬의 수
# line 46 : nums를 집합 자료형 변환하여 중복 제거후 다시 리스트 변환
# line 47 : 중복을 제거한 nums의 길이가 result과 크거나 같으면 가질 수 있는 최대 종류는 result과 같다.
# line 49 : nums의 길이가 작은 경우 그 만큼의 종류를 가질 수 있다.

# 문제풀이(2)
def solution(nums):
    answer = 0
    result = len(nums) / 2 
    nums = list(set(nums)) 
    if len(nums) >= result:
        answer = result     
    elif len(nums) < result: 
        answer = len(nums) 
    return answer

# 다른사람의 Best 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))