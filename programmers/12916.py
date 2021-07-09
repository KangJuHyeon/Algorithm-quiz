def solution(s):
    answer = True
    result = s.lower()
    
    pcount = result.count("p")
    ycount = result.count("y")
    
    if(pcount == ycount):
        return answer
    else:
        return False

# 만약에 p, y의 개수가 같은 경우 True, 아닐 경우 False를 반환하라.
# count() 함수를 사용하여 개수를 파악하고, 조건문에 들여보내면 끝? (다시)
# count() 함수를 사용해서 변수에 담고, 그 변수를 조건문에 이용해 풀어보자.

# 한줄 요약 간단한 코드
# 메서드 체이닝을 통해 함수를 이어 조건문을 만들고, 간단하게 리턴하여 값을 얻음
# return s.lower().count("p") == s.lower().count("y")
