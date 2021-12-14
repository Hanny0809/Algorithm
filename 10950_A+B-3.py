import random

ranNum = random.randrange(1, 10)
print(ranNum)

for i in range(ranNum):
    a, b = map(int, input().split())

    print(a + b)


t = int(input())  # 테스트 케이스 개수 t를 입력받음

for _ in range(t):  # t 만큼 반복
    a,b = map(int,input().split())
    print(a+b)
