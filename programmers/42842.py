# 문제 접근
# 카펫의 가로, 세로의 크기를 순서대로 배열에 담으면 된다.
# brown에 가로, 세로, yellow의 가로, 세로

# <조건>
# a >= b
# 2a + 2b - 4 = brown
# (a-2) * (b-2) = yellow
# 2. 2a + 2b = brown + 4
# 3. ab - 2a - 2b + 4 = yellow

# ab - brown - 4 + 4 = yellow
# ab = yellow + brown

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1, total+1):
        if (total / i) % 1 == 0:
            a = total / i
            print(a)
            print(i)
            if a >= i:
                if 2 * a + 2 * i == brown + 4:
                    return [a, i]
    return answer
print(solution(10, 2))