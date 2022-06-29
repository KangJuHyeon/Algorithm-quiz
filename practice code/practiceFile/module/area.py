print('area 모듈 이름: {}'.format(__name__))

PI = 3.14

# 원의 면적을 구하는 함수
def circle(radius):
    return PI * radius * radius

# 정사각형의 면적을 구하는 함수
def square(length):
    return length * length

# 스크립트처럼 사용해보기
# print(circle(2) == 12.56) # 결과 값: True
# print(circle(5) == 78.5) # 결과 값: True
# print(square(2) == 4) # 결과 값: True
# print(square(5) == 25) # 결과 값: True

if __name__ == '__main__':
    print(circle(2) == 12.56)
    print(circle(5) == 78.5)
    print(square(2) == 4) 
    print(square(5) == 25) 
    
# __name__
# __main__