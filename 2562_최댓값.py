# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 예를 들어, 서로 다른 9개의 자연수 3, 29, 38, 12, 57, 74, 40, 85, 61
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

numsList = []
for i in range(9):
    numsList.append(int(input()))

maxNum = max(numsList)
maxIndex = numsList.index(maxNum) + 1

print(maxNum)
print(maxIndex)

'''
9개의 정수를 numList에 담기 위해 리스트 선언을 해주고 
for 문을 이용하여 numList에 입력받은 정수들을 추가(append이용)해준다.
최댓값은 파이썬 내장함수 (max)를 이용하여 구하고,
인덱스는 리스트명.index를 이용하여 구해준다. 인덱스는 0부터 이므로, 1을 더해주었다. 
'''