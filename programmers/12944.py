# 첫 번째 풀이 
def solution(arr):
    return sum(arr) / len(arr)
    
# 두 번째 풀이 numpy 라이브러리 활용
import numpy
def solution(arr):
    answer = numpy.mean(arr)
    return answer

# 세 번째 풀이 statistics 라이브러리 사용
def solution(arr):
    answer = statistics.mean(arr)
    return answer

# 파이썬 평균 구하기
# 1. statistics 라이브러리 활용하기 (이 라이브러리는 여러 수학 함수가 포함되어 있다.)
# 2. sum() / len()을 사용하여 파이썬 목록의 평균 찾기 
# sum(list) = 주어진 목록의 합계를 얻는다.
# len(list) = 목록의 길이를 반환한다.
# 3. numpy.mean()을 사용하여 파이썬 목록의 평균 찾기
# 4. python 2에서 sum() /float(len())을 사용하여 python 목록의 평균 찾기
# mean = sum(data) / float(len(data))  
# float 부분을 없애고 len(data)로 대체해도 된다. 그대신 소수점이 없어진다.