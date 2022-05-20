# 입국 심사를 기다리는 n명을 모두 심사하는데 걸리는 최소 심사 시간

# 임의의 시간 동안 몇 명이 심사 받을 수 있는지 확인하고 이 값을 최소로 만들기
# 시간의 최소, 최대 범위를 구하고 중간 값이 n명을 심사 할 수 있는 시간인지 확인하며 이분 탐색을 진행한다.
# 중간 값 시간 동안, n명보다 많은 심사 기능 -> 중간 값 기준 왼쪽 범위를 탐색
# 중간 값 시간 동안, n명보다 적게 심사 가능 -> 중간 값 기준 오른쪽 범위를 탐색
# 임의의 시간동안 몇 명을 심사할 수 있는지 확인하는 방법

# 문제풀이(1)
def solution(n, times):
    answer = 0
    # right는 가장 비효율적으로 심사했을 때 걸리는 시간
    # 가장 긴 심사시간이 소요되는 심사관에게 n 명 모두 심사받는 경우이다.
    left = min(times)
    right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        checked = 0
        for time in times:
            # people은 모든 심사관들이 mid분 동안 심사한 사람의 수
            checked += mid // time
            # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나간다.
            if checked >= n:
                break
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우
        if checked >= n:
            answer = mid
            right = mid - 1
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우
        elif checked < n:
            left = mid + 1
    
    return answer
print(solution(6, [7, 10]))

# 문제풀이(2)
def solution(n, times):
    answer = 0
    start = 1
    # 최악의 경우: 가장 오래 걸리는 심사위원에게 모두 심사 받는 경우
    end = max(times) * n
    while start <= end:
        people = 0 # 입국 심사 완료된 사람 수
        mid = (start + end) // 2 # mid 시간 동안 입국심사가 가능한지 판단
        print("mid", mid)
        print(times)
        for time in times:
            # 입국 심사가 가능한 사람 수
            people += mid // time
        print("people", people)
        # n 이상 심사 = mid로 가능하지만 더 가능할 수 있으니
        # 일단 answer 에 저장하고 최소 mid 분 찾기
        if people >= n:
            answer = mid
            end = mid - 1
        # n보다 적은 수 심사 = mid로는 부족
        else:
            start = mid + 1

    return answer
print(solution(6, [7, 10]))