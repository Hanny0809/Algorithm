# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

n = int(input())
nums = []

for i in range(n):
    nums.append(int(input()))
# num_list = sorted(nums)
nums.sort()

for i in nums:
    print(i)
# for i in range(len(nums)):
#     print(num_list[i])

'''
변수 n에 개수를 입력받고, 입력받을 숫자들을 리스트로 담기 위해 변수 nums에 리스트 선언
개수(n)만큼 for문 반복하고, 리스트의 append함수를 이용하여 nums들을 입력받아 추가해줌 
리스트의 sort()함수를 이용하여 오름차순으로 정렬해줌
정렬된 수들을 for문을 이용하여 출력한다 
'''

