# ROT13(백준)

# 문제풀이(1)
S = input()

word = ""
for i in S:
    if 'a' <= i <= 'z':
        ascii_num = ord(i) + 13
        print("az", ascii_num)
        if ascii_num > 122:
            print("z를 넘어감", ascii_num)
            ascii_num -= 26
            print("넘어간 숫자-26", ascii_num)
        word += chr(ascii_num)
    elif 'A' <= i <= 'Z':
        ascii_num = ord(i) + 13
        print("AZ", ascii_num)
        if ascii_num > 90:
            print("Z를 넘어감", ascii_num)
            ascii_num -= 26
            print("넘어간 숫자-26", ascii_num)
        word += chr(ascii_num)
    else:
        print("공백,특수문자", ascii_num)
        word += i
print(word)

# 문제풀이(2)
S = input()

for i in S:
    if i.islower():
        print(chr(97+(ord(i)+13-97)%26), end='')
    elif i.isupper():
        print(chr(65+(ord(i)+13-65)%26), end='')
    else:
        print(i,end='')
