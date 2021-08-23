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
# 카운팅을 하여 모든 경우를 정확히 계산
# 이중포문을 사용할 것

scores = [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]

answer = ''
# 유일한 최고점 또는 유일한 최저점(max, min)

# avg = (학생들의 과제 총 점수) / (과제를 카운팅한 수)
# 90점 이상
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