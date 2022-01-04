# 문제접근
# HEAD(문자), NUMBER(숫자), TAIL(남는 것 .png) 나눠줘야 한다.
# 나누기 전에 문자열이 대소문자 구분없어야하고, 숫자 값에 따라 정렬되어야 한다.

# 수도코드(1)
import re
def solution(files):
    answer = []
    box = []
    for key, value in enumerate(files):
        print(key, value)
        number = re.findall('\d+', value) # 파일 중 숫자부분을 찾아낸다.
        # print(number)
        head = value[:value.index(number[0])].lower()
        print(head)
        # print(value.index(number[0]))
        # tail = value[value.index(number[0]):]
        box.append([head, int(number[0]), key])
    print(box)

    # box를 head순으로 정렬하고 같다면, number순으로 정렬해준다.
    box.sort(key=lambda x: (x[0], x[1]))
    print(box)
    
    for i in box:
        print(files[i[2]])
        answer.append(files[i[2]])
    return answer
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

# 문제풀이(1)
def solution(files):
    answer = []
    for i in files:
        head, number, tail = '', '', ''
        number_check = False
        for j in range(len(i)): # 문자열 자르기
            if i[j].isdigit(): # 처음 나오는 숫자부터는 number로 숫자라면
                number += i[j] 
                number_check = True
            elif not number_check: # 숫자가 아니라면 문자가
                head += i[j]
            else: # 아니고, 남는것이라면
                tail = i[j:]
                break

        answer.append((head, number, tail))

    answer.sort(key=lambda x: (x[0].upper(), int(x[1]))) # HEAD 우선, NUMBER 차선으로 정렬

    return [''.join(a) for a in answer] # 원래 형태로 문자열 만들어서 반환
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

# 다른사람의 풀이(1)
import re
def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    print(temp)
    sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))
    print(sort)
    return [''.join(s) for s in sort]
print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))