def solution(phone_book):
    answer = True
    phone_book.sort()

    for phone in range(len(phone_book)-1):
        if phone_book[phone] in phone_book[phone+1]:
            return False

    return answer

# 만약 정렬을 한다면 자연스럽게 짧은 길이의 문자열이 앞으로 온다.
# 비교도 앞-뒤 만 하면 되기 때문에 쉽게 풀 수 있다.

# 내가 이해가 안됐던 부분은 range(len(phone_book)-1) 이 부분이었는데 
# phone_book 배열에 -1 을 하는 이유는 인덱스 수를 세려면 -1 을 하는 것이 맞다. 이 부분이 이해가 안됐다는게 부끄럽다.