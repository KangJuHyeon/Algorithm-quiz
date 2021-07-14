def solution(s):
    answer = sorted(s, reverse = True)
    answer = "".join(answer)
    return answer


# sorted(s) 오름차순 정렬
# "".join() 함수로 리스트안에 원소를 이어붙인다.
# [::-1]

# 리스트 정렬하는 방법
# 1. 원본 리스트의 변경 없이, 리스트를 정렬하는 방법 sorted 함수
# 2. 리스트의 항목들을 정렬(sorting)하되, 원래의 리스트 자체를 정렬시켜 버리는 sort() 함수
# 3. 정렬(sorting) 순서 바꾸기, 역순(내림차순) 정렬하기 reverse 파라미터 사용
# new_fruits = sorted(fruits, reverse = True)
# fruits.sort(reverse = True)

# 한 줄 요약
# return ''.join(sorted(s, reverse=True))