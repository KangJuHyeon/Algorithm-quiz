def solution(phone_book):
    answer = True
    hash_map = {} # 딕셔너리
    
    # 등장한 숫자들을 count 딕셔너리로 만든다.
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        
    # 다시 숫자들을 꺼낸뒤
    for phone_number in phone_book:
        temp = ""
        for number in phone_number: #숫자 하나씩 뜯어보기
            temp += number
            # 딕셔너리 키로 같은게 있지만 전체 숫자는 다른 경우
            if temp in hash_map and temp != phone_number:
                answer = False
                
    print(hash_map)
    return answer