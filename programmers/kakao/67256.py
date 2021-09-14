# 문제 읽기
# 스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀 있습니다.
# 이 전화 키패드에서 왼손과 오른속의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
# 맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며,
# 엄지손가락을 사용하는 규칙은 다음과 같습니다.

# 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
# 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
# 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
# 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
# 4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

# 순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때,
# 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 함수를 작성하시오.

# 문제 접근
# 오른손잡이이고, 3, 6, 9의 값일 때 'R'이라는 문자열을 빈 배열에 담는다.
# 왼손잡이이고, 1, 4, 7의 값일 때 'L'이라는 문자열을 빈 배열에 담는다.
# 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 땐 두 엄지손가락의 키패드 위치에서 
# 더 가까운 엄지손가락이 눌러야된다.
# 왼손의 위치와 오른손의 위치를 어떻게 구하여야하는가?

# 수도코드(1)
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'

left = '*'
right = '#'
lthumbs = [1, 4, 7]
rthumbs = [3, 6, 9]
cthumbs = [2, 5, 8, 0]

answer = []
for i in numbers:
    if i in lthumbs:
        print(i)
        answer += 'L'
        latest_lthumbs = i
        print(answer)
    elif i in rthumbs:
        print(i)
        answer += 'R'
        latest_rthumbs = i
        print(answer)
    elif i in cthumbs: # 가운데 키패드에 i값이 포함되어 있을 경우
        a = abs(cthumbs.index(i) - latest_lthumbs)
        b = abs(cthumbs.index(i) - latest_rthumbs)
        if a < b: # 왼손잡이 왼손 엄지가 cthumbs보다 가까울 경우 => 왼손잡이 왼손 엄지로 누른다.
            print(i)
            answer += 'L'
            latest_lthumbs = i
            print(answer)
        elif a > b: # 오른손잡이 오른손 엄지가 cthumbs보다 가까울 경우 => 오른손잡이 오른손 엄지로 누른다.
            print(i)
            answer += 'R'
            latest_rthumbs = i
            print(answer)
    else:
        if hand == 'right':
            print(i)
            answer += 'R'
            latest_rthumbs = i
            print(answer)
        else:
            print(i)
            answer += 'L'
            latest_lthumbs = i
            print(answer)
print(answer)


# 수도코드(2)
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = 'right'
right = '*' # 오른손의 현재 위치(시작점)
left = '#' # 왼손의 현재 위치(시작점)

right_handle = [3, 6, 9]
left_handle = [1, 4, 7]
center_handle = [2, 5, 8, 0]

keypad = {1:[0, 0], 2:[0, 1], 3:[0, 2], 
          4:[1, 0], 5:[1, 1], 6:[1, 2], 
          7:[2, 0], 8:[2, 1], 9:[2, 2], 
          '*':[3, 0], 0:[3, 1], '#':[3, 2]}

answer = []
for i in numbers:
    # 3, 6, 9을 누르는 경우 오른손
    if i in right_handle:
        answer += 'R'
        right = i # 오른손의 위치
        # print(answer)
    # 1, 4, 7을 누르는 경우 왼손
    elif i in left_handle:
        answer += 'L'
        left = i # 왼손의 위치
        # print(answer)
    # 2, 5, 8, 0을 누르는 경우
    elif i in center_handle:
        print(keypad[right])
        # print(keypad[i][0] - keypad[right][0])
        a = abs(keypad[i][0] - keypad[right][0])
        b = abs(keypad[i][1] - keypad[right][1])
        ab = a + b
        c = abs(keypad[i][0] - keypad[left][0])
        d = abs(keypad[i][1] - keypad[left][1])
        cd = c + d
        if ab < cd: # 현재 오른손잡이의 엄지손가락이 center_handle의 값에 가까울 경우 => 오른손잡이의 엄지로 누른다.
            answer += 'R'
            right = i
        elif ab > cd: # 현재 왼손잡이의 엄지손가락이 center_handle의 값에 가까울 경우 => 왼손잡이 엄지로 누른다.
            answer += 'L'
            left = i
        # 왼손의 위치와 오른손의 위치를 어떻게 구하여야하는가?
        # 두 엄지손가락의 거리가 같을 때, 오른손잡이는 오른 엄지를, 왼손잡이는 왼손 엄지로 누른다.
        else:
            if hand == 'right':
                answer += 'R'
                right = i # 오른손의 위치
            else:
                answer += 'L'
                left = i # 왼손의 위치
print(answer)

# 문제 풀이(1)
def solution(numbers, hand):
    right = '*' # 오른손의 현재 위치(시작점)
    left = '#' # 왼손의 현재 위치(시작점)

    right_handle = [3, 6, 9]
    left_handle = [1, 4, 7]
    center_handle = [2, 5, 8, 0]

    keypad = {1:[0, 0], 2:[0, 1], 3:[0, 2], 
            4:[1, 0], 5:[1, 1], 6:[1, 2], 
            7:[2, 0], 8:[2, 1], 9:[2, 2], 
            '*':[3, 0], 0:[3, 1], '#':[3, 2]}

    answer = []
    for i in numbers:
        # 3, 6, 9을 누르는 경우 오른손
        if i in right_handle:
            answer += 'R'
            right = i # 오른손의 위치
        # 1, 4, 7을 누르는 경우 왼손
        elif i in left_handle:
            answer += 'L'
            left = i # 왼손의 위치
        # 2, 5, 8, 0을 누르는 경우
        elif i in center_handle:
            a = abs(keypad[i][0] - keypad[right][0])
            b = abs(keypad[i][1] - keypad[right][1])
            ab = a + b
            c = abs(keypad[i][0] - keypad[left][0])
            d = abs(keypad[i][1] - keypad[left][1])
            cd = c + d
            if ab < cd: # 현재 오른손잡이의 엄지손가락이 center_handle의 값에 가까울 경우 => 오른손잡이의 엄지로 누른다.
                answer += 'R'
                right = i
            elif ab > cd: # 현재 왼손잡이의 엄지손가락이 center_handle의 값에 가까울 경우 => 왼손잡이 엄지로 누른다.
                answer += 'L'
                left = i
            # 두 엄지손가락의 거리가 같을 때, 오른손잡이는 오른 엄지를, 왼손잡이는 왼손 엄지로 누른다.
            else:
                if hand == 'right':
                    answer += 'R'
                    right = i # 오른손의 위치
                else:
                    answer += 'L'
                    left = i # 왼손의 위치
    return ''.join(answer)
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))