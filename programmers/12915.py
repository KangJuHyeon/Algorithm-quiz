def solution(strings, n):
    answer = []
    for i in strings:
        answer.append(i[n]+i)  # n번째 문자를 앞에 붙인다.
        answer.sort()
        
    return [i[1:] for i in answer] 
    # strings의 n번째 인덱스 값을 문자열 맨 앞에 붙이고 정렬한다.
    # 반환할 때 반복문을 이용해서 붙였던 문자를 제거한다.

# 빈 배열안에 정렬된 값들이 들어간다.
# n번째 인덱스를 기준으로 정렬된 값을 구하면 된다.
# 그 값에서 슬라이싱해서 한 글자씩만 따서 리턴해보자.

    # def solution(strings, n):
    # n번째 문자를 맨 앞으로 복사한 뒤 정렬하면 사전 순으로 될 것 같다. 
    # ["sun", "bed", "car"] => i[n번쨰 값(인덱스 값)] + i(리스트에서 나온 값) = temp
    # temp = []
    # for i in strings :
    #     temp.append(i[n]+i)
    #     temp.sort()
    
    # 복사한 문자를 지우고 answer에 문자열을 넣는다
    # answer = []
    # for i in temp :
    #     i = i[1:]
    #     answer.append(i)
    # return answer