# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

n = int(input())

c = 0   # count 변수를 두고 0으로 초기화
for i in range(1, n+1):    # 1부터 n까지 for 문을 돌림
    c += 1                  # count를 1씩 증가시킴
    print('*' * c)

'''
우선 n개의 개수를 입력받았다.
1부터 n까지 for문을 돌리고, c(count)변수를 0으로 초기화시키고 
for 문 안에서 1씩 증가시키도록 설정하였다
그리하여 '*'이 하나씩 증가하여 출력된다. 
'''