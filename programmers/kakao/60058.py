# 문제접근
# 올바른 괄호일 경우, 올바르지 않은 괄호일 경우를 잘 생각해야될 것 같다.
# 재귀적(?) 함수를 만들어서 "(" + "" + ")"를 붙여주는 함수를 만들어야하나?
# 문제가 조금 이상하다. 붙이는 함수, 안붙여져있다면 그 문자열을 뒤집는 함수, 만약 붙여서 올바른 괄호라면 리턴
# 재귀함수로 리턴값의 대한 이해가 중요할 것 같다. 마지막엔 class, main function의 리턴값이 출력되도록

# 수도코드(1)
def solution(p):
    answer = ''
    
    # 올바른 괄호일 경우 이 로직을 사용
    def function_1(p):
        for i in p:
            # i가 '('부터 시작할 경우
            if i == '(':
                answer += i
                print(answer)
            # i == ')' 인 경우
            else: 
                if i == '': # 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
                    answer = ''
                else: # 빈 문자열이 아닐경우
                    answer += i
                    print(answer)

    # 문자열 w를 균형잡힌 괄호 문자열 u, v로 분리하는 함수
    def function_2(p):
        box = []
        u, v = 0, 0
        return (u, v)
    
    # 4. 문자열 u가 올바른 괄호 문자열이 아닐경우
    # 4-4 u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙인다.
    def function_3(p):
        box_2 = []

    # w가 매개변수로 들어올 경우
    def function_4(w):
        # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환한다.
        if not w:
            return ''
        # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리해라.
        # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
        u, v = function_2(w)
        # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
        # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        # 4-3. ')'를 다시 붙입니다. 
        return '(' + function_4(v) + ')'
        
    return function_4(p)
print(solution("(()())()")) # "(()())()"
print(solution(")("))       # "()"
print(solution("()))((()")) # "()(())()"

# 문제풀이(1)
# 문자열 w를 u, v로 분리하는 함수
def separation(w):
    right_bracket = 0
    left_bracket = 0

    for i in range(len(w)):
        if w[i] == '(':
            right_bracket += 1
        else:
            left_bracket += 1
        if right_bracket == left_bracket:
            return w[:i + 1], w[i + 1:]

# 올바른 괄호인지 확인하는 함수
def check(u):
    stack = []
    
    for i in u:
        print(i)
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(w):
    answer = ''
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환한다.
    if not w:
        return ''
    
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리해라.
    u, v = separation(w)

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    if check(u):
        return u + solution(v)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        answer += '('
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        answer += solution(v)
        # 4-3. ')'를 다시 붙입니다. 
        answer += ')'
        
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        for i in u[1:len(u) - 1]:
            # print(i)
            if i == '(':
                answer += ')'
            else:
                answer += '('
        
        return answer
print(solution("(()())()")) # "(()())()"
print(solution(")("))       # "()"
print(solution("()))((()")) # "()(())()"

# 문제풀이(2)
def solution(p):
    p = list(p)

    # 2. 문자열 w를 두 균형잡힌 괄호 문자열 u, v로 분리하는 함수
    def separation(w):
        left_cnt = 0
        right_cnt = 0
        # cut_idx = 0
        for i in range(len(w)):
            if w[i] == '(':
                left_cnt += 1
            elif w[i] == ')':
                right_cnt += 1
            # if left_cnt == right_cnt:
            #     cut_idx = i
            #     break
        u, v = w[0: i + 1], w[i + 1:]
        
        return (u, v)
    
    # 올바른 괄호 문자열인지 확인하는 함수
    def check(u):
        stack = []
        idx = 0
        while idx < len(u):
            first_idx = u[idx]
            if not stack:
                stack.append(first_idx)
            elif stack[-1] == '(' and first_idx == ')':
                stack.pop(-1)
            else:
                stack.append(first_idx)
            idx += 1
            
        if stack:
            return False
        else:
            return True  
    
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행하는 함수. 
    # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
    def create(u):
        u.pop(0)
        u.pop(-1)
        if not u:
            return []
        else:
            for i in range(len(u)):
                if u[i] == '(':
                    u[i] = ')'
                else:
                    u[i] = '('
            return u
        
    def main(w):
        # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
        if len(w) == 0:
            return []
        # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
        # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
        u, v = separation(w)
        # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
        if check(u):
            return u + main(v)
        
        # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
        else:
            # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
            new_u = create(u)
            # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
            # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
            # 4-3. ')'를 다시 붙입니다. 
            return ['('] + main(v) + [')'] + new_u
            
    return (''.join(main(p)))
print(solution("(()())()")) # "(()())()"
print(solution(")("))       # "()"
print(solution("()))((()")) # "()(())()"

# 문제풀이(3)
# 균형잡힌 괄호 문자열을 찾기 위한 함수, 올바른 괄호인지도 확인하는 함수
def parse(str):
    correct = True
    left = 0
    right = 0
    stack = []

    for i in range(len(str)):
        if str[i] == '(':
            left += 1
            stack.append('(')
        else:
            right += 1
            if len(stack) == 0:
                correct = False
            else:
                stack.pop()
        if left == right:
            return i + 1, correct

    return 0, False

def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if len(p) == 0:
        return p
    
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
    pos, correct = parse(p)
    u = p[:pos]
    v = p[pos:]

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
    if correct:
        return u + solution(v)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
    # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
    # 4-3. ')'를 다시 붙입니다.
    answer = '(' + solution(v) + ')'
    # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
    for i in range(1, len(u) - 1):
        if u[i] == '(':
            answer += ')'
        else:
            answer += '('
    # 4-5. 생성된 문자열을 반환합니다.
    return answer
print(solution("(()())()")) # "(()())()"
print(solution(")("))       # "()"
print(solution("()))((()")) # "()(())()"