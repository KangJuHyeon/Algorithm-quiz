def solution(left, right):
    answer = 0
    
    for i in range(left, right+1): # left 부터 right까지 1씩 증가하는 for문 ex) 13, 17 => 13, 14, 15, 16 => 그래서 right + 1
        cnt = 0                    # 약수의 개수를 카운트할 변수(상자)
        for j in range(1, i+1):    # 1부터 i까지 증가하며 약수를 찾아낸다
            if i % j == 0:         # 약수 구하기
                cnt += 1           # 약수라면 개수를 증가시켜준다. 이 부분이 JS에선 증감문 cnt++
        if cnt % 2 == 0:           # 홀수인지 짝수인지 판별한다.
            answer += i            # 짝수라면 더하고,
        else:
            answer -= i            # 홀수라면 빼준다.
            
    return answer

# 이중 포문을 사용하여 left부터 right까지를 순회하고,
# j의 값을 i까지 순회하여 i를 j로 나누어 떨어지는 수를 카운트해서
# 홀수 개의 약수인지, 짝수 개의 약수인지 구별하면 될 것 같다.