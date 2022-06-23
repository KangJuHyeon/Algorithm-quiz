# 문자열 분석(백준)
import sys 

while True:
    N = sys.stdin.readline().rstrip('\n')

    lower, upper, number, blank = 0, 0, 0, 0
    
    for i in N:
        # 소문자
        if i.islower():
            lower += 1
        # 대문자
        elif i.isupper():
            upper += 1
        # 숫자
        elif i.isdigit():
            number += 1
        # 공백
        elif i.isspace():
            blank += 1

    if not N:
        break

    print(f"{lower} {upper} {number} {blank}")