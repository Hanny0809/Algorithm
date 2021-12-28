# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(n):
    if a[i] < x:
        print(a[i], end=' ')


'''
입력받을 정수개수 n 과 비교대상 정수 x 변수를 입력받고,
수열 a 변수를 입력받고, 이를 리스트로 변환한다
n만큼 반복문을 돌리고,
if문을 이용하여 수열a의 수를 인덱스로 하나씩 불러와 x보다 작으면 출력시킨다. 
'''