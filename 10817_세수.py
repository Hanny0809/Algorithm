# 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.

nums = list(map(int, input().split()))
sorted_nums = sorted(nums)

print(sorted_nums[1])

'''
nums 변수를 두어 세 수를 입력받고 리스트로 변환해준다.
입력받은 nums리스트를 sorted()를 이용해서 정렬해주고 정렬해준 것을 sorted_nums에 다시 할당해준다.
인덱스를 이용해 두번째로 큰 값을 출력한다. 
'''