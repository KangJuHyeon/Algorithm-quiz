def solution(n):
    result = list(str(n))
    result.sort(reverse = True)
    return int("".join(result))

# 처음 문제 풀이(내 생각)
# 정수라서 split(), join() 메서드가 필요가 없음
# 그렇다면? 정수를 내림차순 오름차순 해주는 메서드를 찾아서 사용하자.
# 위에 생각은 틀렸다. 다시 풀어보자.

# 문제 풀이 및 공부
# 이 문제에선 정수를 어떻게 정렬할 지 고민하고, 정렬은 정수는 안되고, 문자열만 된다는 것을 알았다.
# 정렬은 나열 형만 가능해서 주어진 정수를 문자열로 형 변환 후에 사용해야 된다.
# 1. 정수를 문자열로 바꾸기 : str(n)
# 2. 문자열을 내림차순으로 정렬 : sorted(), reverse()
# 3. 리스트를 하나의 문자열로 조인 : .join()
# 4. 문자열을 정수로 바꿔서 리턴 : int()

# Best 풀이
    return int("".join(sorted(list(str(n)), reverse = True)))