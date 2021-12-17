# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
# 하지만, 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력하시오.

n = int(input())

for i in range(1, n+1):
    for j in range(n-i):
        print(' ', end="")
    for j in range(i):
        print('*', end="")
    print('')


'''
어제 별찍기와는 다른점이 있다면 오른쪽 정렬이 되어 출력이 되어야 한다는 점이다.
우선 for문을 돌리고, for문 내부에
하나는 빈칸을 생성하고 다른 하나는 별을 찍는 두개의 for문을 만들었다. 
'''