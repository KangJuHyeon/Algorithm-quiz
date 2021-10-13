# 문제 접근
# 정렬 알고리즘의 삽입 정렬을 이용해서 풀어볼 예정이다.
# 두 번째 인덱스의 값을 첫 번째 인덱스와 비교하여 작은 값이 앞으로 오도록 해준다.
# random? 정렬? 다 아닌 것 같은 느낌

# 수도코드(1)
import random

def solution(numbers):
    answer = ''
    random.shuffle(numbers)
    for i in range(len(numbers)):
        for j in numbers:
            print(j)
            answer += str(j)
        # print(numbers[i-1])
        # if numbers[i] < numbers[i-1]:
        #     answer += str(i)
        # answer += str(i)
        # if max(answer) < answer:
    print(answer)
    return answer
print(solution([6, 10, 2]))

# 문제풀이(1)
def solution(numbers):
    answer = list(map(str, numbers))
    answer.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(answer)))
print(solution([6, 10, 2]))
print(solution([0,0,0,0])) 

# 이 문제를 마치고 나서 회고
# 결국 못 풀었다. lambda 함수 사용하는 방법에 대해서 알아가는 것 같다.
# 람다 함수식은 항상 보기는 했지만 편견이 있었던 것 같다.
# 람다 함수식을 사용하는 정도면 정말 실력이 좋아야만 사용할 수 있겠지? 그런 편견인 것 같다.
# 결국 하기 싫어서 배우기 싫어서 자신한테 핑계를 된 것 같다.
# 이번 계기로 람다 함수식을 연습할 수 있는 기회가 있어서 좋았다.