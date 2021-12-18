# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 첫번째 방식
n = int(input())

nums = list(map(int,(input().split())))
print(min(nums), max(nums))

'''
n개의 정수를 입력받고, nums를 리스트 배열로 묶어서 입력받는다 
파이썬에 내장되어 있는 최소(min), 최대(max)함수를 이용하여 풀어주었다.
'''

# 두번째 방식
n = int(input())

nums = list(map(int,(input().split())))

min = nums[0]
max = nums[0]

for i in nums[1:]:
    if i < min:
        min = i

    if i > max:
        max = i

print(min, max)

'''
n에 입력 개수를 받고, nums에 정수를 입력받는다. input().split()을 이용하여 공백으로 구분한다.
max와 min에 각 각 nums의 첫번째 요소를 넣어준다.
for문에서 nums의 2번째 요소부터 마지막 요소까지 차례로 비교해준다.
max보다 크면, max값을 바꿔주고, min보다 작으면, min값을 바꿔준다.
'''