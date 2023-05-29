# 영수증
X = int(input()) # 총 금액
N = int(input()) # 구매한 물건의 종류의 수

total = 0

for i in range(N):
    a, b = map(int, input().split())

    total += a * b

if X == total:
    print("Yes")
else:
    print("No")