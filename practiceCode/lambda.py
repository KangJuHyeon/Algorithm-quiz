# 람다(lambda)
# lambda 인자 : 표현식

def hap(x, y):
    return x + y
print(hap(10, 20))

# 위에 함수를 람다 형식으로 표현
print((lambda  x,y: x + y)(10, 20))

# map함수는 리스트에서 원소를 하나씩 꺼내서 함수를 적용시킨 결과를 새로운 리스트에 담아준다.
# map(함수, 리스트)
print(list(map(lambda x: x ** 2, range(5))))

# reduce(함수, 시퀀스)
# 시퀀스(문자열, 리스트, 튜플)
from functools import reduce
print(reduce(lambda x, y: x + y, [0, 1, 2, 3, 4]))
# 먼저 0과 1을 더하고, 그 결과에 2, 3, 4를 더하는 순서입니다.

print(reduce(lambda x, y: y + x, 'abcde'))

# filter(함수, 리스트)
# 리스트에서 필터처럼 원하는 값을 걸러서 나오게 해준다.
# 파이썬 2
# 파이썬 2의 결과는 filter의 값이 객체라고만 나온다.
print(filter(lambda x: x < 5, range(10)))

# 파이썬 2, 3
print(list(filter(lambda x: x < 5, range(10)))) 

# 홀수를 돌려주는 필터 만들기 
print(list(filter(lambda x: x % 2, range(10))))
