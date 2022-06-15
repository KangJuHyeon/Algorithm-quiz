# # 파일 읽기 -> 'r'
# with open('/Users/kangjuhyeon/Documents/my-project/Algorithm-quiz/practice code/fs/chicken.txt', 'r') as f:
#     print(type(f))
#     for line in f:
#         print(line)

# # strip
# with open('/Users/kangjuhyeon/Documents/my-project/Algorithm-quiz/practice code/fs//chicken.txt', 'r') as f:
#     print(type(f))
#     for line in f:
#         print(line.strip())

# # 코딩에 빠진 닭 문제 풀이(1)
# with open('/Users/kangjuhyeon/Documents/my-project/Algorithm-quiz/practice code/fs/chicken.txt', 'r') as f:
#     total = 0
#     for line in f:
#         line_list = line.strip().split(" ")
#         sales = line_list[1]
#         total += int(sales)
#     total = total / 31
# print(total)

# # 파일 쓰기 -> 'w'
# with open('/Users/kangjuhyeon/Documents/my-project/Algorithm-quiz/practice code/fs/new_file.txt', 'w') as f:
# 		f.write("Hello world!\n")
# 		f.write("My name is Codeit.\n")

# # 파일 추가 -> 'a'
# with open('/Users/kangjuhyeon/Documents/my-project/Algorithm-quiz/practice code/fs/new_file.txt', 'a') as f:
# 		f.write("Hello world!\n")
# 		f.write("My name is Codeit.\n")

# # 단어장 만들기 문제 풀이(1)
# with open('/Users/kangjuhyeon/Documents/my-project/Algorithm-quiz/practice code/fs/vocabulary.txt', 'w') as f:
        
#         while True:
#             english = input("영어 단어를 입력하세요: ")
#             kor = input("한국어 뜻을 입력하세요: ")
            
#             if english == 'q':
#                 break

#             if kor == 'q':
#                 break
            
#             f.write(f'{english}: {kor}\n')
            
# # 단어 퀴즈 문제 풀이(1)
# with open('/Users/kangjuhyeon/Documents/my-project/Algorithm-quiz/practice code/fs/vocabulary.txt', 'r') as f: 

#     for word in f:
#         english_answer = word.split()[0][:-1]
#         korean_quiz = word.split()[1] + ': '
        
#         if input(korean_quiz) == english_answer:
#             print("맞았습니다!")
#         else:
#             print(f"아쉽습니다. 정답은 {english_answer}입니다.")

# # 단어 퀴즈 문제 풀이(2)
# with open('/Users/kangjuhyeon/Documents/my-project/Algorithm-quiz/practice code/fs/vocabulary.txt', 'r') as f: 
#     for line in f:
#         data = line.strip().split(": ")
#         english_word, korean_word = data[0], data[1]
        
#         # 유저 입력값 받기
#         guess = input("{}: ".format(korean_word))
        
#         # 정답 확인하기
#         if guess == english_word:
#             print("맞았습니다!\n")
#         else:
#             print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))

# 고급 단어장 문제 풀이(1)
import random

with open('/Users/kangjuhyeon/Documents/my-project/Algorithm-quiz/practice code/fs/vocabulary.txt', 'r') as f: 
    vocab = {}
    
    for word in f:
        data = word.strip().split(": ")
        english_answer, korean_quiz = data[0], data[1]
        vocab[english_answer] = korean_quiz
        print(f"data: {data}, english_answer: {english_answer}, korean_quiz: {korean_quiz}, vocab[english_answer]: {vocab[english_answer]}")

    while True:
        # 랜덤한 문제 받아오기
        keys = list(vocab.keys()) # 고급 단어장이 담긴 리스트
        index = random.randint(0, len(keys)-1) # 랜덤해서 나온 퀴즈 인덱스
        english_answer = keys[index] # 영어 단어 정답
        korean_quiz = vocab[english_answer] # 한글 단어 정답
        print(f"keys: {keys}, index: {index}, english_answer: {english_answer}, korean_quiz: {korean_quiz}")
        
        # 유저 입력값 받기
        guess = input(f"{korean_quiz}: ")

        # 프로그램 끝내기
        if guess == 'q':
            break
    
        # 정답 확인하기
        if guess == english_answer:
            print("맞았습니다!")
        else:
            print(f"아쉽습니다. 정답은 {english_answer}입니다.")
        
