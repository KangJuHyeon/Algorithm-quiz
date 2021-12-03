# 문제접근
# 가장 먼저 탈락하는 사람의 번호와 
# 그 사람이 자신의 몇 번째 차례에 탈락하는지를 알아보자.
# 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 한다(1)
# word의 단어가 중복되었는지 확인(2)
# 번호, 차례를 어떻게 구함? => %, // 연산자 사용할 것
# 사람을 구할 때 1을 더하는 이유는 문제에서 사람이 1부터 시작하기 때문이고,
# 몇 번째 턴인지 구할 때 1을 더하는 이유는 맨 첫 턴을 1부터 시작하기 때문이다.

# 수도코드(1)
def solution(n, words):
    answer = []
    number = 0 # 번호
    order = 0 # 차례

    answer.append(words[0]) # 앞 글자를 넣어둠으로써 뒤에 글자와 비교
    last = words[0][-1] # 글자의 마지막을 추출하여 넣어놓음
    # print(last)
    for i in range(1, len(words)):
        # print(words[i][0])
        # 앞사람이 말한 단어의 마지막 문자로 시작하는 단어를 말해야 한다(1)
        # word의 단어가 중복되었는지 확인(2)
        if words[i] not in answer and words[i][0] == last:
            answer.append(words[i])
            print(answer)
            last = words[i][-1]
            print(last)
        else:
            number = (i % n) + 1
            print(number)
            order = (i // n) + 1
            print(order)
            break # 여기서 break를 준 이유는 중간에 never뒤에 now가 나왔을 떄 멈춰야한다. 멈추고 그 값을 리턴해야 한다.
        
    return [number, order]
print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))

# 문제풀이(1)
def solution(n, words):
    answer = []
    for i in range(len(words)):
        # answer가 비어있다면 채워준다.
        if not answer:
            answer.append(words[i])
        else:
            # 만약 answer배열에 word[i]가 포함되어 있다면
            if words[i] in answer: 
                return [i % n + 1, i // n + 1]
            # 만약 잘 진행하다가 중간에 틀렸을 경우, 바로 return
            elif answer[i-1][-1] != words[i][:1]:
                return [i % n + 1, i // n + 1]
            # # 끝말잇기가 틀리지않고 계속 간다면 단어를 모두 통과
            else:
                answer.append(words[i])
    return [0, 0]
print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))