# 공 넣기
N, M = map(int, input().split())
basket = [0] * (N + 1)
print(basket)

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j + 1):
        print("n", n)
        basket[n] = k 
        print("basket", basket[n])

for i in range(1, N + 1):
    print(basket[i], end = ' ')