# 문제풀이(1)
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if i != j:
                answer.append(numbers[i] + numbers[j])
    result = list(set(answer))
    result.sort()
    return result

# 문제풀이(2)
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)): # 중복이 일어나면 안되므로 i+1 설정
            if(numbers[i] + numbers[j]) not in answer: # 만약에 numbers[i] + numbers[j]의 값이 answer에 포함되어 있지 않으면 추가해줘라 answer.append()값을
                answer.append(numbers[i] + numbers[j]) # [2, 3, 4, 5, 6, 7]
    return sorted(answer) # 중복제거된 리스트를 오름차순으로 정렬해서 리턴

# 문제 접근
# 서로 다른 Index에 있는 두 수를 뽑아야 하기 때문에 이중 포문을 사용하자.
# 중복도 제거해야될 것 같다.
# 중복제거, 모든 조합
# 파이썬에는 포함(Containment) 연산자를 ( in, not in ) 제공하며, 객체 in (not in) 시퀀스의 형태로 사용 가능하다.
# if A in B : B안에 A가 있으면 True
# if A not in B : B안에 A가 없다면 True
# if i != j: <- 이 부분도 맞는말이다.