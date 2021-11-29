# 문제접근
# 3킬로그램, 5킬로그램 설탕을 N킬로그램으로부터 하나씩 빼보자.
# 18-5, 13-5, 8-5, 3이 됐을 때 3킬로그램 설탕 봉지로 나눈다. => 0
# 그렇다면 저 과정을 카운팅한 값이 봉지갯수

N = int(input()) # N킬로그램 설탕

cnt = 0

while True:
    if N % 5 == 0:
        cnt += N / 5
        break
    else:
        N -= 3
        cnt += 1

    if N < 0:
        cnt = -1
        break
print(int(cnt))
