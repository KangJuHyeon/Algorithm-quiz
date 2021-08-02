# 문제
# a는 '월' b는 '일'을 가르킨다. 2016년 a월 b일이 무슨 요일인지 리턴하는 함수를 완성하라.
# SUN,MON,TUE,WED,THU,FRI,SAT => a = 5 b= 24, 2016년 5월 24일은 TUE를 리턴한다.
# a = 5, b = 24 => TUE

# 문제 접근
# 각 요일이 들어있는 배열(list)을 만들고, 날짜 라이브러리가 따로 있을 것 같으니 검색해본다.

# 문제풀이(1)
import datetime

def solution(a, b):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    # result = days[datetime.date(a,b).weekday()]
    return days[datetime.date(2016,a,b).weekday()]


# 문제풀이(2)
import datetime

def solution(a,b):
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return days[datetime.datetime(2016, a, b).weekday()]