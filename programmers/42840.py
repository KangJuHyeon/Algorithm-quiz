# 문제 읽기
# 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 함수를 작성하라.

# answers = [1,2,3,4,5], return = [1]
# answers = [1,3,2,4,2], return = [1,2,3]

# 입출력 예 #1
# 수포자 1은 모든 문제를 맞혔습니다.
# 수포자 2는 모든 문제를 틀렸습니다.
# 수포자 3은 모든 문제를 틀렸습니다.
# 따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

# 입출력 예 #2
# 모든 사람이 2문제씩을 맞췄습니다.

# 문제 접근
# 완전탐색 방법처럼 무식하게 for문이나 while문을 돌려서 모든 경우의 수를 체크해서 정답을 얻는다.
# 문제의 정답은 1,2,3,4,5 중 하나이다.
# 수포자들은 어떻게 생각해야되는 것인지?
# answers 배열에서 제일 많이 나온 숫자를 카운팅해서 answer 빈 배열안에 넣는다.
# 다른 방법은 조금 힘들다. 무식하게 대입해보자.

# 수도코드(1)
answers = [1, 3, 2, 4, 2]
# [1, 2, 3, 4, 5]
# [1, 3, 2, 4, 2]

answer = []

cnt1 = 0 # 수포자1이 몇번을 찍었는지 카운트
cnt2 = 0 # 수포자2이 몇번을 찍었는지 카운트
cnt3 = 0 # 수포자3이 몇번을 찍었는지 카운트

player1 = [1, 2, 3, 4, 5]                # 수포자1
player2 = [2, 1, 2, 3, 2, 4, 2, 5]       # 수포자2
player3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 수포자3

for i in range(len(answers)):
    if answers[i] == player1[i % 5]:
        cnt1 += 1
    if answers[i] == player2[i % 8]:
        cnt2 += 1
    if answers[i] == player3[i % 10]:
        cnt3 += 1

Immersive = max(cnt1, cnt2, cnt3) # 수포자 1,2,3 리스트 중 가장 큰 값을 이머시브 변수에 할당

if Immersive == cnt1: # 만약 이머시브 리스트와 cnt1의 값이 같다면
    answer.append(1)  # 빈 answer 배열에 1을 넣어준다.
if Immersive == cnt2: 
    answer.append(2)
if Immersive == cnt3:
    answer.append(3)
print(answer)

# 문제풀이(2)
def solution(answers):
    answer = []
    cnt = [0,0,0]

    player1 = [1, 2, 3, 4, 5]
    player2 = [2, 1, 2, 3, 2, 4, 2, 5]
    player3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == player1[i % 5]:
            # print(player1[i % 5])
            cnt[0] += 1
        if answers[i] == player2[i % 8]:
            # print(player2[i % 8])
            cnt[1] += 1
        if answers[i] == player3[i % 10]:
            # print(player3[i % 10])
            cnt[2] += 1

    for i in range(3):
        if cnt[i] == max(cnt): # 3명의 수포자 배열 중 제일 많이 맞춘 수포자 배열과 같다면
            answer.append(i+1) # 빈 배열에 추가시켜준다. 1, 2, 3 => 0, 1, 2
    return answer

print(solution([2, 1, 2, 3, 2, 4, 2, 5]))

# line 63 : 수포자들이 맞은 점수를 세는 cnt 리스트를 만들고 0으로 초기 값 설정
# line 65~67: 무식하게 수포자1, 수포자2, 수포자3 이런식으로 문제의 규칙을 그대로 설정
# line 70 : 정답 배열의 길이만큼 반복이 될 때 answers의 i인덱스의 값과 player의 i의 패턴이 반복하는 숫자만큼 나눈 나머지 인덱스 cnt에서 하나씩 증가(print로 돌려보면 이해하기 쉬움)
# line 80 : 위에 반복문이 끝나면 cnt[0,0,0] 3번을 돌아서 cnt 리스트에서 제일 큰 값이랑 같으면
# line 82 : 빈 answer 리스트 안에 배열 인덱스+1을 넣어준다.
# line 83 : return answer


# 다른사람이 푼 Best 풀이
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result

# enumerate 함수를 사용하여 answers를 {key: value} 이런식으로 나눠준 것 같다.
# answer키 값이 pattern1의[idx % 5]와 같다면 => {0: 1}, {1: 2}, {2: 3}, {3: 4}, {4: 5}
# score 리스트안에 담긴 카운팅 초기 값에 +1을 한다.
# score 리스트도 enumerate 함수를 사용해 {key: value} 이런식으로 나눠준다.
# 만약 {idx: s}가 max(score)와 같다면
# result란 빈 배열에 넣어준다. 
# 어떤 값을? idx라는 배열 인덱스+1의 값을 => 길이 len(1,2,3), 배열은 [0,1,2] => 길이와 배열은 다르다.