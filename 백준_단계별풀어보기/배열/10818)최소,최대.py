# 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다.
# 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.
# 모든 정수는 -1,000,000보다 크거나 같고,
# 1,000,000보다 작거나 같은 정수이다.

# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

# 예제 입력
# 5
# 20 10 35 30 7

# 예제 출력
# 7 35

# 내가 푼 오답
# n = int(input())
# arr = list(map(int, input().split()))
# min = 1000000
# max = 1
# for i in arr:
#     if min > i:
#         min = i
#     if max < i:
#         max = i
# print(min, max)

# 두번째 시도
n = int(input())
arr = list(map(int, input().split()))
min = arr[0]
max = arr[0]
for i in arr:
    if min > i:
        min = i
    if max < i:
        max = i
print(min, max)

# 처음에 틀린 이유
# 처음에 최솟값, 최댓값을 선언하였을 때 문제에 있는 범위로 했지만 오답이 떴고,
# 입력받은 배열의 값을 임의로 정해서 비교하니 정답이 나왔다.
