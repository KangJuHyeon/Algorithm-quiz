print('run 모듈 이름: {}'.format(__name__))

import area
# import area as ar # area를 ar 변수라는 것으로 사용하겠다는 뜻이다.
from area import square as sq 
# from area import * # area라는 모듈에 함수를 모두 사용하겠다는 뜻이다. 이것은 파이썬 커뮤니티에선 권장하지 않는다고 한다.
# from area import circle # 이런식으로도 사용할 수 있다. circle 함수만 사용하겠다는 뜻이다.

print(area.circle(2))
print(area.square(3))
print(area.PI)
print(sq(3))

# print(dir(area))
print(dir()) # 모듈의 이름만 정의되고 모듈 안에 있는 함수는 정의되지 않는다.

# x = float(input('원의 반지름을 입력해 주세요: '))
# print('반지름이 {}인 원의 면적은 {}입니다.\n'.format(x, area.circle(x)))

# y = float(input('정사각형의 변의 길이를 입력해 주세요: '))
# print('변의 길이가 {}인 정사각형의 면적은 {}입니다.\n'.format(y, area.square(y)))

print('run 파일 실행됨')
