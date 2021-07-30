# 문제 접근
# x는 index를 가리킨다.
# in 키워드, find()함수 사용해볼 것
# 특정한 문자열이 포함된 문자열 찾기
def solution(seoul):
    x = seoul.index("Kim")
    if "Kim" not in seoul:
        return 0
    else:
        return f"김서방은 {x}에 있다"