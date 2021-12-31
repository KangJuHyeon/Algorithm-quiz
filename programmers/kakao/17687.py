# 문제접근
# n은 진법, t는 미리 구할 숫자의 갯수, 문자열, 게임에 참가하는 인원 m, 튜브의 순서 p

def solution(n, t, m, p):
    answer = ''
    alpha = ['A', 'B', 'C', 'D', 'E', 'F']
    number = 0
    result = '0'

    while len(answer) < t:
        temp = '' # 초기화 박스
        a = number

        while a > 0:
            a, b = divmod(a, n)
            if b >= 10:
                temp = alpha[b-10] + temp
                print(temp)
            else:
                temp = str(b) + temp

        result += temp
        print(result)
        answer = ''
    
        for i in range(p-1, len(result), m):
            answer += result[i]
        
        number += 1

    return answer[:t]
print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))