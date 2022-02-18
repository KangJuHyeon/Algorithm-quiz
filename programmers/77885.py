# 문제풀이(1) - 비트연산 활용
# 효율성 문제에서 out
def solution(numbers):
    answer = []
    
    for i in numbers:
        # 만약 짝수라면?
        if i % 2 == 0:
            answer.append(i+1)
            print(answer)
        # 아니고, 홀수라면?
        else:
            # 1, 2, 3 => 최하위 비트 0 위치 찾기 rfind, index
            # print(i)
            last_word = (i+1) & (-i) # 1 AND 0 => 0
            # print(last_word) # 8
            # 4 -> 최하위 비트 0을 1로 바꾸기
            zero_word = i | last_word # 1 or 1 = 1 아니면 0 or 1 = 1
            # print(zero_word) # 15
            temp = (zero_word & (~(last_word) >> 1)) # ~ 연산자 -> 비트를 1이면 0으로, 0이면 1로 반전시킴. (비트 NOT 연산)
            # >> 연산자 -> 부호를 유지하면서 지정한 수만큼 비트를 전부 오른쪽으로 이동시킴. (right shift 연산)
            # 15 AND 8(-5) -> 8의 2진수: 01000 NOT 연산하면 (00111)
            # 01111 AND 111(00111) -> 2진수로 따지면?
            # print(temp) # 11
            print((~(last_word)>> 1)) # -5
            # 01000(8) -> 10111(15) -> >>1 0111(7)
            answer.append(temp)

    # for i in numbers:
    #     bit = bin(i)[2:]
    #     print(bit)
    #     last_word = bit[:2]
    #     print(last_word)
    return answer
print(solution([2, 7])) # [3, 11]

# 문제풀이(2) - 파이썬 bin 내장함수 활용, 10진수로 변환
# 효율성 문제에서 out
def solution(numbers):
    answer = []

    for i in numbers:
        # 짝수일 때
        bit = list('0' + bin(i)[2:])
        print(bit)
        idx = ''.join(bit).rfind('0')
        print(idx)
        bit[idx] = '1'
        print(bit[idx])
        print(bit)
        
        # 홀수일 때
        print(i)
        if i % 2 == 1:
            bit[idx+1] = '0'
            print(bit[idx+1])
            print(bit)
        
        answer.append(int(''.join(bit), 2))
        print(answer)

    return answer
print(solution([2, 7])) # [3, 11]

# 문제 풀이
# 1) 짝수의 경우
# 만약, 4라면 이진수로 100 이다. 
# 4보다 크면서 2개 이하로 다른 수를 찾으면 101 이다.
# 즉, 가장 뒤에 있는 0을 1로 바꿔주면 된다.

# 2) 홀수의 경우
# 만약, 7이라면 이진수로 0111 (바꿀때 편의를 위해 앞에 0을 붙인다)
# 먼저 짝수의 경우처럼 가장 뒤에 있는 0의 인덱스(idx)를 찾아 1로 바꿉니다. 
# 그럼 1111 이 된다.
# bit[idx] = '1'
# 그런 다음 idx+1 의 인덱스 값을 0으로 바꾼다. 
# 그럼 1011이 되고 답이 된다. 10진수로 변환 => 11
# bit[idx+1] = '0'


# 최종 문제 풀이
def solution(numbers):
    answer = []
    
    for i in numbers:
        i = int(i)
        # 만약 짝수라면?
        if i % 2 == 0:
            answer.append(i+1)
        # 아니고, 홀수라면?
        else:
            # 1, 2, 3 => 최하위 비트 0 위치 찾기 rfind, index
            last_word = (i+1) & (-i) # 1 AND 0 => 0
            # 4 -> 최하위 비트 0을 1로 바꾸기
            zero_word = i | last_word # 1 or 1 = 1 아니면 0 or 1 = 1
            temp = (zero_word & (~(last_word) >> 1))
            answer.append(temp)

    return answer
print(solution([2, 7])) # [3, 11]

# 안풀리던 이유가 numbers의 배열의 부수 값을 정수로 변환하면 풀린다.
# 이유는 정확히 모르겠다. 개인적으로 numbers의 배열의 안에 있는 값은 정수라고 생각하기 때문이다.