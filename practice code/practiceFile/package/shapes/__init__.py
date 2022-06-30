print('__init__.py 파일 실행')

# from shapes import area, volume
# from shapes.area import circle, square

# 상수를 __init__ 파일에 선언하고 다른 파일에서 가져다 사용하기
PI = 3.14

# 특수 변수
__all__ = ['area', 'volume']