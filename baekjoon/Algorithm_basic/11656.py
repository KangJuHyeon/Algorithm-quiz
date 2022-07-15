# 접미사 배열(백준) - 실버4

S = input().lower()
answer = []

for i in range(len(S)):
    answer.append(S[i:])

answer.sort()
for i in answer:
    print(i)