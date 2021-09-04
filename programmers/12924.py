# 문제 읽기
# Finn은 요즘 수학공부에 빠져 있습니다. 
# 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게되었습니다.
# 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

# 1 + 2 + 3 + 4 + 5 = 15
# 4 + 5 + 6 = 15
# 7 + 8 = 15
# 15 = 15

# 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 리턴하는 함수를 만들어라.

# 문제 접근
# n = 15니까 이중 포문을 돌아서
# 1보단 크고, n까지 도는 for문 그리고 중복되면 안되니까
# i부터 도는 포문을 하나 더 돌아서 카운팅을 센다.

# 수도코드(1)가 문제풀이(1)가 되버렸다.
def solution(n):
    answer = 0
    for i in range(1, n+1):
        cnt = 0
        # print(i)
        for j in range(i, n+1):
            # print(j)
            cnt += j
            print(cnt)
            if cnt == n: # 만약에 카운팅을 센 숫자가 n과 같다면
                answer += 1
                break
            elif cnt > n: # 만약에 카운팅을 센 숫자가 n보다 크다면 for문을 빠져나온다.
                break
    return answer
print(solution(15))

            