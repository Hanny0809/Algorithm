# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 1.for 반복문 활용
n = int(input())

result = 1
for i in range(1, n+1, 1):
    result *= i

print(result)

# 2. 재귀함수 활용

def factorial_result(n):
    if (n > 1):
        return n * factorial_result(n-1)
    else:
        return 1

num = int(input())
print(factorial_result(num))


# 라이브러리 활용
import math

number = int(input())
print(math.factorial(number))


'''
팩토리얼 (factorial) : 1부터 지정된 수까지 모든 수의 곱, 계승이라고 표현함 

1번 풀이
사용자에게서 팩토리얼 숫자n을 입력을 받음, 결과에 출력할 result변수에 1을 할당한다.
for 반복문을 이용하여 입력받은 수까지 반복을 수행하며 result에 해당 값을 곱한다.

2번 풀이
재귀함수를 사용
재귀함수란? 함수 내부에서 자기 자신을 호출하는 함수 
def를 통해 factorial_result(n)함수를 정의
입력받은 파라미터 값이 1보다 크면 입력받은 수 * factorial_result(n-1)값을 리턴하도록 하였다. 

3번 풀이
math 라이브러리에서 제공하는 factorial 함수 이용
'''

