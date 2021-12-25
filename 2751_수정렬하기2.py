# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오. 단 수는 절대 중복되지 않는다

n = int(input())
nums = set()    # 중복 제거를 위해 set()함수 사용

for i in range(n):
    nums.add(int(input()))
nums_list = list(nums)
nums_list.sort()

for num in nums_list:
    print(num)

    '''
    변수 n에 개수를 입력받고, 입력받을 숫자들을 중복없이 담기 위해 set()함수 이용
    개수(n)만큼 for문 반복하고, set의 add함수를 이용하여 nums들을 입력받아 추가해줌 
    nums를 다시 리스트로 변환 시킴 
    리스트의 sort()함수를 이용하여 오름차순으로 정렬해줌
    정렬된 수들을 for문을 이용하여 출력한다 
    '''