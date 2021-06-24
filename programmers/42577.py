def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True

# 내장함수 zip을 사용한 풀이
# zip은 함수 안의 각 리스트, 튜플, 문자열에 대하여 각 요소를 짝지어 주는 함수이다.
# 반환 값이 list는 아니기 때문에 for문의 변수에 대입하는 것이 아니라면 list처리를 해줘야 한다.
# startswith는 꽤 직관적인 함수로 p2가 p1으로 시작되면 True 아니면 False를 반환한다.