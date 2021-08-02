# 파이썬 datetime 요일 계산하는 방법, 특정 날짜의 요일 계산법 : weekday(), calendar.weekday()

# date.weekday() 정수로 요일을 반환한다. 월요일은 0이고 일요일은 6이면
# date(2020, 12, 2).weekday() # 2 
# 그럼 수요일을 반환한다. ["월", "화", "수", "목", "금", "토", "일"] 인덱스 2 => 요일로 반환
# weekday()함수를 사용하기 위해서는 datetime 모듈을 먼저 import합니다.

import datetime

days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]

a = datetime.datetime.today().weekday()
print(a)
print(days[a])
# 실행 결과
# 0
# 월요일
# 리스트 자료형에 월요일부터 일요일까지 담고, weekday()가 리턴하는 정수값으로 리스트 자료형의 값을 가져오면 간단하게 요일 정보를 알 수 있습니다.

# 그럼 특정일자의 요일정보는 어떻게 확인할까요?
# 2020년 9월 12일은 무슨 요일 일까요?
# import datetime

# days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
# b = days[datetime.date(2020, 9, 12).weekday()]
# print(b)
# 토요일

# 함수(def)로 만들어서 유틸리티처럼 필요할 때 호출하여 사용할 수도 있습니다.
import datetime

def get_today_days():
    days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    return days[datetime.datetime.today().weekday()]

print(f"오늘은{get_today_days()}입니다.")

# 실행결과
# 오늘은월요일입니다.

import datetime

def get_days(year, month, day):
    days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    return days[datetime.date(year, month, day).weekday()]

year = 2020
month = 8
day = 2
print(f"{year}년 {month}월 {day}일은 {get_days(2020,8,20)}입니다.")
# 실행결과
# 2020년 8월 2일은 목요일입니다.

# calendar()함수를 사용하여 년도별 달력을 볼 수 있습니다.
import calendar

print(calendar.calendar(2021))

# calendar.prmonth()함수를 사용하면 원하는 년 월을 달력만 출력할 수 있습니다.

import calendar

calendar.prmonth(2021, 5)