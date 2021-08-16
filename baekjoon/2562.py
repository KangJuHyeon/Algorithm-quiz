# 문제
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 예를 들어, 서로 다른 9개의 자연수
# 3, 29, 38, 12, 57, 74, 40, 85, 61
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# 입력
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

# 수도코드(1)
# 리스트로 해도 결국 답은 똑같으니 되는 것 아닌가 싶어서 풀어보았지만 틀렸다고 나옴ㅠ
result = list(map(int, input().split()))

print(max(result))
print(result.index(max(result))+1)

# 문제풀이(1)
# 1차원 배열을 선언하고 그 안에 입력값을 주고 max함수를 이용해 최댓값을 구하고,
# 그 최댓값의 배열 index를 찾아내서 +1 해주면 된다.
answer = []
for i in range(1, 10):
    n = int(input())
    answer.append(n)

print(max(answer))
print(answer.index(max(answer))+1)
