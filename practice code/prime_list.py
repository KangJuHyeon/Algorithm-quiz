# def solution(n):
# 	# 2부터 n까지의 숫자 배열 만들기
#     num_set = set(range(2, n+1)) # 2 ~ 10까지라고 하면 [2, 3, 4, 5, 6, 7, 8, 9]

#     for i in range(2, n+1): # 
#         if i in num_set: # 배수 제거
#             num_set -= set(range(i*2, n+1, i))

#     answer = len(num_set)

#     return answer

# print(solution(10))

n = 10
# 2부터 n까지의 숫자 배열 만들기
num_set = set(range(2, n+1)) # 2 ~ 10까지라고 하면 {2, 3, 4, 5, 6, 7, 8, 9, 10}
print(num_set)
for i in range(2, n+1): # 
    if i in num_set: # 배수 제거
        num_set -= set(range(i*2, n+1, i))
        print(num_set)

answer = len(num_set)
print(answer)