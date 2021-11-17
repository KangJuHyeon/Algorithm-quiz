# 문제접근
# 채팅방에 들어오고 나가거나, 닉네임을 변경했을 경우를 생각해야된다.
# 닉네임을 변경하면 채팅방에 있는 기록들도 다같이 변화한다.
# 채팅방을 들어왔을 때, 채팅방을 나갔을 때 기록이 남는다.
# 공백을 기준으로 문자열을 나눠야 이름을 얻을 수 있지 않을까?
# 배열로는 확실하게 값을 저장하고 변경할 수 없다. {}
# 모든 유저는 [유저 아이디]로 구분한다.
# 닉네임을 변경했을 때 그 닉네임은 어디에 저장되어 있어야 한다.
# 변경되었을 때, 그 값이 변경되어서 Log에 뿌려지면 된다.

def solution(record):
    answer = []
    log = {}

    for i in record:
        word = i.split(" ") # 공백을 기준으로 문자열 나눔
        status = word[0] # 첫 단어 상태를 담는다.
        uid = word[1]    # 고유 uid를 담는다.

        if status != "Leave": # 채팅방을 나가지 않았을 때
            nickname = word[2] # 닉네임을 담는다.
            log[uid] = nickname # 딕셔너리에 담아서 uid가 1234, 4567일 때 닉네임을 담는다.
            print(log)

    for i in record:
        word = i.split(" ") # 공백 기준 문자열 나눔
        
        status = word[0] # 첫 단어 상태를 담는다.
        uid = word[1]    # 고유 uid를 담는다.

        if status == "Enter": # 첫 단어가 Enter일 때(채팅방에 들어왔을 때)
            answer.append(log[uid] + "님이 들어왔습니다.")
        elif status == "Leave": # 첫 단어가 Leave일 때(채팅방을 나갔을 때)
            answer.append(log[uid] + "님이 나갔습니다.")

    return answer
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# 결과 값
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", 
# "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]


# 다른사람의 풀이(1)
# Enter
# Leave
# Change
def solution(record):
    userDict = {}
    answer = []

    for line in record:
        line = line.split(" ")

        if line[0] == "Enter":
            userDict[line[1]] = line[2] # 딕셔너리 uid에 닉네임을 들이는 것
        elif line[0] == "Change":
            userDict[line[1]] = line[2] # Change될 때도 변경된 값만 value값에 바꾸어준다.

    for line in record:
        line = line.split(" ")
        targetString = userDict[line[1]]
        if line[0] == "Enter":
            targetString += "님이 들어왔습니다."
        elif line[0] == "Leave":
            targetString += "님이 나갔습니다."
        else:
            continue
        answer.append(targetString)

    return answer