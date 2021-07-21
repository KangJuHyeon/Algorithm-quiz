# 문제풀이(1)
def solution(arr):
    if len(arr) > 1: # 만약에 arr 길이가 1보다 클 때
        arr.remove(min(arr)) # arr의 제일 작은수를 제거한다.
        return arr
    else:
        return [-1] # 위에 내용이 아니라면 나머지는 [-1]을 리턴
    
# 문제풀이(2)
def solution(arr):
    answer = min(arr) # arr배열에서 가장 작은 수를 찾는 함수 min()을 사용하여 answer에 담는다.
    arr.remove(answer) # remove 함수를 사용하여 arr배열에서 제일 작은 수를 제거한다.
    if not arr: # 만약 arr가 빈 배열이라면 arr배열의 0번째에 -1를 삽입한다.(한 개의 값만 들어있는 배열이라면 자기 자신이 최소값이므로 -1)
        arr.insert(0, -1) # return [-1]도 가능
    return arr

# 문제 접근
# 배열 arr에서 제일 작은 수를 제거하고, 빈 배열일 경우 -1을 리턴
# 빈 배열인지 체크해야 하나?
# 제일 작은 수인지 어떻게 알지? 
# arr에서 제일 작은 수를 제거하고, 새로운 배열에 추가시켜서 풀이를 해?
# remove() 제거하고, min으로 제일 작은 수를 확인하자
# remove(min(arr))