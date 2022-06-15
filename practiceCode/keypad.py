def solution(numbers, hand):
    answer = ''
    
    #지금 손의 위치
    left = '*'
    right = '#'
    
    keypad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    
    for i in numbers :
        # 1, 4, 7의 값이 i가 포함하고 있다면
        if i in [1, 4, 7]:
            answer += 'L'
            left = i
        # 3, 6, 9의 값이 i가 포함하고 있다면
        elif i in [3, 6, 9] :
            answer += 'R'
            right = i
        else:
            for j in range(4):
                if i in keypad[j]:
                    print(j)
                    num_x = keypad[j].index(i)
                    num_y = j
                    print(answer)
                if left in keypad[j]:
                    print(j)
                    l_x = keypad[j].index(left)
                    l_y = j
                    print(answer)
                if right in keypad[j]:
                    print(j)
                    r_x = keypad[j].index(right)
                    r_y = j
                    print(answer)
                    
            l_distance = abs(num_x - l_x) + abs(num_y - l_y)
            r_distance = abs(num_x - r_x) + abs(num_y - r_y)

            if l_distance < r_distance :
                answer += 'L'
                left = i
            elif l_distance == r_distance :
                if hand == 'left' :
                    answer += 'L'
                    left = i
                else :
                    answer += 'R'
                    right = i
            elif l_distance > r_distance :
                answer += 'R'
                right = i
    return answer
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))