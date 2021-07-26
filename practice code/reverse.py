# reverse()와 reversed()의 차이 알아보기

# reverse

# 1. reverse는 list 타입에서 제공하는 함수이다.
l = ['a', 'b', 'c']
t = ('a', 'b', 'c')
d = {'a': 1, 'b': 2, 'c': 3}
s = 'abc'

print(l.reverse())  # list의 순서를 뒤집어줌
# print(t.reverse())  # AttributeError: 'tuple' object has no attribute 'reverse'
# print(d.reverse())  # AttributeError: 'dict' object has no attribute 'reverse'
# print(s.reverse())  # AttributeError: 'str' object has no attribute 'reverse'

# 2. reverse는 값을 반환하지 않고, 단순히 해당 list를 뒤섞어준다.
l = ['a', 'b', 'c']
l_reverse = l.reverse()

print(l_reverse)  # None
print(l)  # ['c', 'b', 'a']

# reversed 알아보기

# 1. reversed는 내장함수로, list에서 제공하는 함수가 아니다.
l = ['a', 'b', 'c']
t = ('a', 'b', 'c')
d = {'a': 1, 'b': 2, 'c': 3}
s = 'abc'

print(reversed(l))  # <listreverseiterator object at 0x101053c10>
print(reversed(t))  # <reversed object at 0x101053b50>
print(reversed(d))  # TypeError: argument to reversed() must be a sequence
print(reversed(s))  # <reversed object at 0x101053c10>

# 딕셔너리는 시퀀셜한 타입이 아니므로 지원하지 않는다.
# 즉, l[0], l[1] 과 같이 순차적인 인덱스로 접근할 수 없기떄문에 지원하지 않는다.

# 2. reversed는 'reversed' 객체를 반환한다.
l = ['a', 'b', 'c']
t = ('a', 'b', 'c')
s = 'abc'

print(reversed(l))  # <listreverseiterator object at 0x101053c10>
print(reversed(t))  # <reversed object at 0x101053b50>
print(reversed(s))  # <reversed object at 0x101053c10>

# tuple과 str의 경우 'reversed' 객체를 반환하는 것을 볼 수 있다.
# 하지만 list의 경우 특이하게 listreverseiterator를 반환한다.
# reversed 객체를 tuple 혹은 list로 바꾸어 사용하려면 아래처럼 사용해야 한다.

l = ['a', 'b', 'c']
t = ('a', 'b', 'c')

print(list(reversed(l)))  # ['c', 'b', 'a']
print(tuple(reversed(t)))  # ('c', 'b', 'a')

# 물론, list로 만든 listreverseiterator 객체를 반드시 list로 만들어야 되는 것은 아니고,
# tuple로 만든 reversed 객체를 반드시 tuple로 만들어야하는건 아니다.
# 문자열로 만들려면 굳이 list나 tuple로 바꿀 필요 없이 join을 통해 요소들을 연결해주면 된다.
l = ['a', 'b', 'c']
print(''.join(reversed(l)))  # 'cba'

n = 12345
print(list(map(int, reversed(str(n))))) # [5, 4, 3, 2, 1]

# 슬라이싱으로 역순으로 만드는 방법도 있다.
# 파이썬에서는 슬라이싱이 제일 빠르다고 하니 이게 성능이 좋지않을까? 라는 생각을 가지고있다.
num = 12345
arr = []
result = str(num)
for i in result:
    arr.append(int(i))
print(arr[::-1])