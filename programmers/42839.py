# 문제 접근
# 문자열을 정수로 바꾸고 소수의 갯수를 카운팅하여 풀어보자.
# "011"에서 막히는데 어째 [7, 17, 71]이 이상한 값 같다.
# 그냥 정수 갯수와 리스트를 이용한 갯수를 카운팅해도 안되는 것은 다른 방법으로 접근해야 한다.
# 이 문제는 완전 탐색 기법 중 하나를 써야한다 뒤늦게 깨달았다.
# for문 if문, 비트마스크, 재귀 함수, 순열, BFS/DFS

# 수도코드(1)
def solution(numbers):
    n = int(numbers)
    answer = 0
    count = 0
    for i in range(1, n+1):
        print(i)
        for j in range(2, i):
            print(j)
            if i % j == 0:
                answer = 1
        if answer == 0: # answer가 0과 같을 때
            count += 1
            print(f"{i}는 소수입니다.")
        else:
            print(f"{i}는 소수가 아닙니다.")
    print(f"소수의 개수는 {count}입니다.")
    return count

# 수도코드(2)
def solution(numbers):
    answer = 0
    count = []
    for i in range(len(numbers)):
        print(i)
        for j in range(2, i):
            print(j)
            if i % j == 0:
                answer = 1
        if answer == 0: # answer가 0과 같을 때
            count.append(i)
            print(count, "\n", "소수의 개수는", len(count),"입니다.")
    return count


# 문제풀이(1)
from itertools import permutations

arr = [] # 소수의 갯수를 셀 리스트 선언

# 소수 검사하는 로직
# 1. 우선 소수가 맞다면 배열(arr)에 넣어주는 소수 검사 함수를 구현
def prime_number_Check(num):
    n = int(num)
    # 2부터 (n - 1)까지의 모든 수를 확인하며
    if n != 1 and n != 0:
        for i in range(2, n):
            # n이 해당 수로 나누어 떨어진다면
            if n % i == 0:
                return False # 소수가 아님
    else:
        return False

    arr.append(n) # 소수이다.

# 원소들을 중복 검사하는 로직
def solution(numbers):
    for i in range(1, len(numbers) + 1): # 1, 2
        # itertools의 permutations을 이용하여 각 숫자로 이루어질 수 있는 숫자들을 배열로 만들어준다.
        permute = list(map(''.join, permutations(list(numbers), i)))
        print(permute)
        
        for j in permute:
            prime_number_Check(j) # 소수 검사

    answer = set(arr) # 원소들을 중복 검사
    print(answer)
    return len(answer)
# print(solution("17")) # 3
print(solution("011")) # 2


# 다른사람의 코드(1)
from itertools import permutations
 
 
def solution(numbers):
    answer = []
    #string을 한 글자식 list로 담으려면 list(string)
    numbers= list(numbers)
 
    #순열을 사용한다.
    for i in range(len(numbers)):
        arr = list(permutations(numbers, i+1)) #순열로 변환 (튜플)
        arr = list(map(lambda x: int(''.join(list(x))) ,arr))
 
        for number in arr:
            isAnswer = True
            if number >1 and number not in answer:
                for i in range(2, number):
                    
                    if number % i == 0:
                        isAnswer = False
                        break
                if isAnswer == True:
                    answer.append(number)
 
 
    return len(list(set(answer)))