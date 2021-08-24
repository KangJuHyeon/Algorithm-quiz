# 문제 접근
# 학생들이 자기 자신을 평가한 점수가 유일한 최고점 또는 유일한 최저점이라면,
# 그 점수는 제외하고 평균을 구한다.
# 그 후에 그 평균을 "DA" 이런식으로 리턴하라.

# 90점 이상 : A
# 80점 이상 90점 미만 : B
# 70점 이상 80점 미만 : C
# 50점 이상 70점 미만 : D
# 50점 미만 : F

# 문제 풀이
# 자기 자신을 평가한 점수를 어떻게 판단하지?
# for문을 돌려서 배열의 순서를 자기 자신을 평가한 점수?
# 2차원 배열의 값의 첫 번째를 어떻게 가져오지? 이중 포문으로 i, j 가로 세로 값을 가져와야한다.
# 카운팅을 하여 모든 경우를 정확히 계산?
# 이중포문을 사용할 것
# 빈 배열에 자신들의 평가 점수를 넣고 평균을 구한다.
# 그 뒤에 answer 문자열에 학점으로 변환한 값을 넣어주면 된다.


# 수도코드(1)
scores = [[70,49,90],[68,50,38],[73,31,100]]
# [[50,90],[50,87]]
# [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]

answer = ''
# 유일한 최고점 또는 유일한 최저점(max, min)
for i in range(len(scores)):
    # 학생들에게 평가된 점수를 담기위해 빈 배열 선언
    arr = [] 
    for j in range(len(scores)):
        score = scores[j][i]
        print(score)
        arr.append(score)
        # print(arr)
    
    # min, max를 사용하여 학생들이 자기 자신을 평가한 점수가 유일한 최고점, 유일한 최저점이라면 해당 점수 제거
    if arr[i] == max(arr) and arr.count(arr[i]) == 1:
        # print(arr[i])
        del arr[i]
    elif arr[i] == min(arr) and arr.count(arr[i]) == 1: 
        # print(arr[i])
        del arr[i]

    # avg = (학생들의 과제 총 점수) / (과제의 수)
    avg = sum(arr) / len(arr)   

    # 학점으로 변환하는 과정 => switch문이 생각남; 왜지?
    if avg >= 90:
        answer += 'A'
    elif 80 <= avg < 90:
        answer += 'B'
    elif 70 <= avg < 80:
        answer += 'C'
    elif 50 <= avg < 70:
        answer += 'D'
    else:
        answer += 'F'
print(answer)

# 문제풀이(1)
def solution(scores):
    answer = ''
    for i in range(len(scores)):
        arr = []
        for j in range(len(scores)):
            score = scores[j][i]
            arr.append(score)
        
        # 만약 학생들의 평가된 점수가 제일 큰 점수가 같거나, 학생들의 평가된 점수 중 1과 같다면, arr[i]값을 제거한다.
        if arr[i] == max(arr) and arr.count(arr[i]) == 1:
            del arr[i]
        elif arr[i] == min(arr) and arr.count(arr[i]) == 1:
            del arr[i]

        avg = sum(arr) / len(arr)
        
        # 학점 변환
        if avg >= 90:        # 90점 이상일 경우
            answer += 'A'
        elif 80 <= avg < 90: # 80점 이상 90점 미만
            answer += 'B' 
        elif 70 <= avg < 80: # 70점 이상 80점 미만
            answer += 'C'
        elif 50 <= avg < 70: # 50점 이상 70점 미만
            answer += 'D'
        else:                # 50점 미만일 경우
            answer += 'F'
    
    return answer

print(solution([[70,49,90],[68,50,38],[73,31,100]]))