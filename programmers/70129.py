# 문제접근
# s가 '1'이 될 때까지 계속해서 s에 이진 변환을 가했을 때, 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 배열에 담아 리턴하라.

def solution(s):
    answer = []

    count = 0 # 이진 변환의 횟수
    zero = 0 # 변환 과정에서 제거된 모든 0의 개수

    while True:
        # 만약 s가 1이라면 정지
        if s == '1':
            break
        # 0을 제거하고 개수를 담아야한다.
        zero += s.count('0')
        print(zero)
        s = s.replace('0', '')
        print(s)
        # 0을 제거 후 길이를 담고, 이진 변환을 하여야한다. => s는 이진 변환 이전
        s = bin(len(s))[2:]
        print(s)
        count += 1
        print(count)
    
    # 3번의 이진 변환을 하는 동안 8개의 0을 제거했으므로, [3,8]을 리턴
    answer = [count, zero]

    return answer
print(solution('110010101001'))
print(solution('01110'))
print(solution('1111111'))

# 다른사람의 문제풀이(1)
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:]
    return [a, b]