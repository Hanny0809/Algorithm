# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

n = int(input())
nums = list(map(int, input()))

while True:
    total  = 0
    for num in nums[0:]:
        total += num
    print(total)
    break
    
'''
N개의 숫자를 공백없이 입력받아 숫자를 모두 합하는 프로그램 작성하기 
우선 변수n으로 숫자를 입력 받고, 변수 nums에 숫자들을 공백없이 리스트로 입력받는다.
이번엔 while문을 활용해보았다. total변수를 두어 0으로 초기화시켰다 
그안에는 for문을 설정하여 nums의 숫자들을 인덱스0부터 모두 더해주었다 
'''