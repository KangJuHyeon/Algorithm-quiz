# 소수 찾기(백준)

N = int(input())
numbers = map(int, input().split())
answer = 0
for num in numbers:
    count = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 n-1까지
            if num % i == 0:
                count += 1  # 2부터 n-1까지 나눈 몫이 0이면 count가 증가
        if count == 0:
            answer += 1  # count가 없으면 소수.
print(answer)