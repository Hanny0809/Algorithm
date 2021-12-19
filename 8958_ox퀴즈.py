'''
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우
그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
'''

n = int(input())

for i in range(n):
    ox = list(input())
    score = 0
    totalScore = 0

    for j in ox[0:]:
        if j == 'O':
            score += 1
        else:
            score = 0
        totalScore += score

    print(totalScore)


'''
테스트 케이스인 변수 n을 입력받고, 문자열 OX를 입력받는다. 입력받은 OX는 리스트로 변환시킨다.
n번 만큼 for문을 돌리고 점수(score)와 총점(totalScore) 을 변수선언하고 0으로 초기화 시켰다.
또 다른 for문은 리스트 ox를 인덱스 0부터로 설정해놓고 문자열이 O이면 1씩 증가하도록 하고
X면 값을 0으로 했다. 
점수의 합은 총점(totalScore)에 할당하였다. 
'''