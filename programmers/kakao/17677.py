# 집합 A = {1, 2, 3}, 집합 B = {2, 3, 4}라고 할 때, 교집합 A ∩ B = {2, 3}, 합집합 A ∪ B = {1, 2, 3, 4}이 되므로, 
# 집합 A, B 사이의 자카드 유사도 J(A, B) = 2/4 = 0.5가 된다. 
# 집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.
# 자카드 유사도는 원소의 중복을 허용하는 다중집합에 대해서 확장할 수 있다. 다중집합 A는 원소 "1"을 3개 가지고 있고, 다중집합 B는 원소 "1"을 5개 가지고 있다고 하자. 이 다중집합의 교집합 A ∩ B는 원소 "1"을 min(3, 5)인 3개, 합집합 A ∪ B는 원소 "1"을 max(3, 5)인 5개 가지게 된다. 
# 다중집합 A = {1, 1, 2, 2, 3}, 다중집합 B = {1, 2, 2, 4, 5}라고 하면, 교집합 A ∩ B = {1, 2, 2}, 합집합 A ∪ B = {1, 1, 2, 2, 3, 4, 5}가 되므로, 
# 자카드 유사도 J(A, B) = 3/7, 약 0.42가 된다.

# 이를 이용하여 문자열 사이의 유사도를 계산하는데 이용할 수 있다. 
# 문자열 "FRANCE"와 "FRENCH"가 주어졌을 때, 이를 두 글자씩 끊어서 다중집합을 만들 수 있다. 
# 각각 {FR, RA, AN, NC, CE}, {FR, RE, EN, NC, CH}가 되며, 교집합은 {FR, NC}, 합집합은 {FR, RA, AN, NC, CE, RE, EN, CH}가 되므로, 
# 두 문자열 사이의 자카드 유사도 J("FRANCE", "FRENCH") = 2/8 = 0.25가 된다.

# 문제접근
# 자카드 유사도 계산? (교집합)/(합집합) * 65536
# 문자열이 주어졌을 때, 두 글자씩 끊어서 다중집합을 만들 수 있다.
# 교집합, 합집합을 어떻게 구할지 생각해봐야된다. => set()을 사용하면 중복값을 제거하기 때문에 x
# 중복을 어떻게 세야될지, 생각해봐야될 것 같다.

# 문제풀이(1)
from collections import Counter
def solution(str1, str2):
    # 대문자와 소문자의 차이는 무시한다.
    str1_word = str1.lower()
    str2_word = str2.lower()
    print(str1_word)
    print(str2_word)
    
    str1_box = []
    str2_box = []
    
    for i in range(len(str1_word)-1):
        print(str1_word[i+1])
        if str1_word[i].isalpha() and str1_word[i+1].isalpha():
            str1_box.append(str1_word[i] + str1_word[i+1])
        print(str1_box)

    for i in range(len(str2_word)-1):
        if str2_word[i].isalpha() and str2_word[i+1].isalpha():
            str2_box.append(str2_word[i] + str2_word[i+1])
        print(str2_box)
    
    # 교집합, 합집합, 다중집합을 만들기 위해, 고유의 원소 값을 만들기위해 Counter 라이브러리 추가
    counter1_box = Counter(str1_box)
    counter2_box = Counter(str2_box)
    print(counter1_box, counter2_box)

    # 카운팅된 값이 아니라 key값의 고유 원소값을 가져오기 위해 elements()함수를 사용
    # {'aa', 'aa'}, {'aa', 'aa', 'aa'} ==> ['aa', 'aa'], ['aa', 'aa', 'aa']
    intersection = list((counter1_box & counter2_box).elements()) # 중복된 값이 있어도되고, word값의 교집합을 구해야한다.
    union = list((counter1_box | counter2_box).elements()) # 중복된 값이 있어도되고, word값의 합집합을 구해야한다.
    print(intersection, union)
    # TypeError: unsupported operand type(s) for &: 'str' and 'str'
    # str타입끼리의 & 연산자를 지원하지 않는다.
    # 해결방법 : Counter 라이브러리를 사용하여 중복값을 세고, key값들을 교집합, 합집합으로 변환한 후 list를 씌워주고, 변수 값에 담았다.

    # 자카드 유사도 계산 => (교집합)/(합집합)
    # 교집합과 합집합이 모두 0인 경우 자카드 유사도가 0인 경우 계산을 할 수 없기때문에, 65536이 출력되도록 한다.
    if len(union) == 0 and len(intersection) == 0:
        return 65536
    else:
        return int(len(intersection)) / len(union) * 65536
    
print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))