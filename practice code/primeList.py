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
        num_set -= set(range(i*2, n+1, i)) # (i * 2)i가 2부터 시작하니까 (2x2=4, 3x2=6, 4x2=8, 5x2=10, (6x2=12) =>{2,3,5,7,9} 10+1, 2)
        print(num_set)

answer = len(num_set)
print(answer)