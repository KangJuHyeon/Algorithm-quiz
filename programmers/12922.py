def solution(n):
    answer = ''
    
    for i in range(n):
        if(i % 2 != 0):
            answer += "박"
        else:
            answer += "수"
            
    return answer

# 만약에 n=4일 때, "수박수박"을 반환하고, n=3일 때 "수박수"를 반환하라.
# 위에 생각으로 풀어보니, 통과는 되지만 정확성 문제에서 막힌다. (다시)
# index n=3, n=4일 때로 생각하자면 
# i = 0일 때, answer = "수"
# i = 1일 때, answer = "수박"
# i = 2일 때, answer = "수박수"
# i = 3일 때, answer = "수박수박"
# i = 4일 때, answer = "수박수박수"
# 만약에 n이 짝수라면 "수"를 반환, 아니라면 "박"을 반환