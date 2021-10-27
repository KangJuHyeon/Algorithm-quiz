# 문제 접근
# 순열과 조합을 사용하여 풀어볼 수 있을 것 같다.
# 순열과 조합 => 시간초과 (다른방법 생각)
# 제일 작은 수를 제거해야하는 방식?은 아닌 것 같다. max, min x
# 3234, 775841을 어떻게? k = 2, 3, 4 제거 했을 때 나오는 방법
# 앞 뒤 비교 후 제거 다음 붙이기
# stack을 이용해서 풀어야 한다는 것을 질문하기에서 깨달았다.

# 수도코드(1)
from itertools import combinations

def solution(number, k):
    answer = list(combinations(list(number), len(number)-k))
    print(answer)
    a = list(map(''.join, sorted(answer, reverse = True)))[0]
    print(a)
    return a
print(solution("1924", 2)) # "94"
print(solution("1231234", 3)) # "3234"
print(solution("4177252841", 4)) # "775841"

# 수도코드(2)
def solution(number, k):
    number = list(number)
    
    i = 0
    while k > 0:
        a = number[i]
        b = number[i+1]
        
        if a != b:
            if a < b: # 1 < 2 비교
                del number[i]
                print(number)
                k -= 1
            else: # 3 < 1 비교
                del number[i+1]
                print(number)
                k -= 1
        else: # 끼워맞춰봄 7 == 7 같을 경우
            i += 2

    return ''.join(number)
print(solution("1924", 2)) # "94"
print(solution("1231234", 3)) # "3234"
print(solution("4177252841", 4)) # "775841"

# 문제풀이(1)
def solution(number, k):
    answer = ''
    stack = []
    for i in number:
        # print(i)
        while stack and stack[-1] < i and k > 0: # 스택이 비어있을 때까지 pop
            stack.pop()
            k -= 1
            print(stack)
            print(k)
            if stack == []:
                break
        stack.append(i)
        print(stack)
        print(k)
    
    # 테스트 케이스 12번 k가 0이 아닐 때 == '999'일 때 9하나 나와야 할 상황일 때
    if k != 0:
        stack = stack[:-k]

    answer = ''.join(stack)

    return answer
print(solution("1924", 2)) # "94"
print(solution("1231234", 3)) # "3234"
print(solution("4177252841", 4)) # "775841"
print(solution('999', 2)) # 9

# 다른사람의 풀이(1)
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)