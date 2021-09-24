# 문제 읽기
# n개의 음이 아닌 정수가 있습니다.
# 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3 

# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 뺴서
# 타겟 넘버를 만드는 방법의 수를 리턴하는 함수를 만들어라.

# numbers = [1, 1, 1, 1, 1], target = 3, return = 5

def solution(numbers, target):
    answer = 0 # 카운팅 
    def dfs(idx, result):
        if idx == len(numbers): # 인덱스가 배열의 길이와 같을 때
            if result == target: # 타겟넘버와 일치하는 값의 갯수를 센다.
                nonlocal answer
                answer += 1
            return 0
    
        dfs(idx + 1, result + numbers[idx])
        dfs(idx + 1, result - numbers[idx])
    dfs(0, 0)

    return answer
print(solution([1, 1, 1, 1, 1], 3))