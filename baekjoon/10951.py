# A+B - 4
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 문제를 잘 읽어보자.
# 입력이 끝날 때까지 A+B를 출력하는 문제. EOF에 대해 알아보세요.

# 보통 EOF란 End of File을 말한다. 파일 입출력 할때 입력이 끝날때 까지 읽어들이는 readline()와 같은 내장 함수 명령을 쓸때 사용된다.
# 이때도 코드 마다 다르겠지만 보통 예외처리를 이용하여 처리한다.

while True:
    try:
        A, B= map(int,input().split())
        print(A+B)
    except:
        break