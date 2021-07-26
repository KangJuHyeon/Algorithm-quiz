# 문제 풀이(1)
# 정수를 문자열로 변환하고, reverse = True 정렬하여 리턴하면 될 것 같다.
def solution(n):
    answer = list(str(n)) # "5", "4", "3", "2", "1"
    answer.sort(reverse = True) # ["5", "4", "3", "2", "1"]
    return int("".join(answer)) # 54321 x
# 정렬 문제가 아닌것인가? 54321 => [54321] 값이 비스무리하게 나온다. 다시 생각해보자.
# 12345 => [] => [5, 4, 3, 2, 1]
# "5", "4", "3", "2", "1" => ["5", "4", "3", "2", "1"] => 54321 x
# "".join()을 사용하게 되면 list가 그냥 정수로 나온다.
# ''.join(리스트)를 이용하면 매개변수로 들어온 ['a', 'b', 'c'] 
# 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환해주는 함수인 것입니다.
# "".join(리스트) 함수는 배열에 담긴 값을 "구분자"를 넣어 배열의 값을 빼내어 나타낼 때 사용된다.
# 자연수를 뒤집으려면 문자열로 변환하여 정렬 reverse를 시켜야된다.
# 정렬 문제가 아니라 뒤집기 문제이다? sort x, reverse o ?

# 문제 풀이(2)
# 정수 n을 문자열로 변환하고, reverse()메서드로 뒤집고,
# 그 값을 담은 상자를 for문으로 순회하고 그 값들을 빈 배열에 int로 담는다.
# 그 값을 리턴한다.
def solution(n):
    result = []
    answer = list(str(n))
    answer.reverse()
    for i in answer:
        result.append(int(i))
    return result

# 문제 풀이(3) *Best
# Str(), resverse() map() int() 활용
# 자연수를 스트링으로 바꿔서 리스트로 묶어주고 => 12345 => "1", "2", "3", "4", "5" => ["1", "2", "3", "4", "5"]
# 그 리스트를 리버스 함. => ["5", "4", "3", "2", "1"] => 정수로 바꿔주면 된다.
# 리버스한 리스트를 정수로 바꿔줘야 하기 때문에 맵으로 바꿔준다. 
# map 함수를 이용해 reverse(str(n))이 값을 int로 바꾸고, list에 담는다.
def solution(n):
    return list(map(int, reversed(str(n))))

# 문제 풀이(4)
# 슬라이싱으로 배열의 역순으로 값을 나오게 하면 된다.
def solution(n):
    answer = list(str(n))
    result = []
    for i in answer:
        result.append(int(i))
    return result[::-1]