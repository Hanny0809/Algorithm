'''
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
'''

n = int(input())

for i in range(n):
    scores = list(map(int, input().split()))
    average = sum(scores[1:]) / scores[0]

    cnt = 0
    for score in scores[1:]:
        if average < score:
            cnt += 1

    rate = cnt / scores[0] * 100
    print(f'{rate:.3f}%')


'''
테스트케이스 개수를 변수n에서 입력받고, 학생수와 학생들의 점수를 리스트로 변환한 변수 scores에 입력받는다. 
이때에 scores[0]은 학생수, scores[1:] 는 점수이다.
평균은 sum(scores[1:] / scores[0]) 으로 구해준다
평균을 넘는 학생수를 구하기 위해 cnt변수를 선언하고 0으로 초기화 시킨다.
score이 average보다 크면 cnt를 1씩 증가시킨다.
평균이 넘는 학생수의 비율을 구한다 (rate = cnt / scores[0] * 100)
'''