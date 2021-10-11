# 벌집 이동 간 간격 1은 1, 1이상부터는 벌집 2, 결국 6간격으로 벌집이 이동
# 1, 6, 12, 18, 24

# 수도코드(1)
N = int(input())
answer = 0

if N <= 7:
    answer += 2
elif 6 < N <= 19:
    answer += 3
elif 19 < N <= 37:
    answer += 4
elif 37 < N <= 61:
    answer += 5
else:
    print('end')
print(answer)

# 문제풀이(1)
N = int(input())

room = 1 # 벌집의 갯수, 1부터 시작해야 58까지 5개
count = 1
while N > room:
    room += 6 * count # 벌집이 6의 배수로 증가한다
    count += 1
print(count)