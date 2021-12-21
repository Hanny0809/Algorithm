'''
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
'''

t = int(input())  # 테스트 케이스 넘버

for i in range(t):
    num, word = input().split()
    for j in word:
        print(j*int(num), end='')
    print()

'''
t 변수에 테스트 케이스 수를 입력받고, t만큼 for문을 반복
반복할 숫자와 문자열을 입력받음. 이때 split은 공백을 기준으로 입력받은 값을 분리시킴
*연산자를 이용하여 입력받은 수만큼 문자열이 반복되도록 함
출력은 공백없이 옆으로 정렬될 수 있도록 end=' ' 을 이용 
end=' ' 값을 입력하는 경우 다음 문자열도 줄 넘김이 되지 않기 때문에 for 문이 끝나면
빈 print()함수를 이용하여 줄 넘김이 되도록 함 
'''