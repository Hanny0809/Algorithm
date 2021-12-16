# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 출력 : Case #1: 1 + 4 = 5

t = int(input())  # 테스트 개수

for i in range(1, t+1):
    a, b = map(int, input().split())

    print(f'Case #{i}: {a} + {b} = {a+b}')
    
'''
바로 전에 풀었던 문제에서 출력부분만 살짝 바꿔서 풀면 되서 빨리 해결했다.
'''