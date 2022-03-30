# 문제
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 예를 들어, 서로 다른 9개의 자연수
# 3, 29, 38, 12, 57, 74, 40, 85, 61
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# 입력
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

# 출력
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

# 예제 입력
# 3
# 29
# 38
# 12
# 57
# 74
# 40
# 85
# 61

# 예제 출력
# 85
# 8

# 첫번째 시도
# arr = []
# max = arr[0]
# for i in arr:
#     i = int(input())
#     arr.append(i)
#     if max > i:
#         max = i
# print(max)
# print(arr[max])

# 두번째 시도
# arr = []
# for i in range(9):
#     arr.append(int(input()))
# for i in arr:
#     if max < i:
#         max = i
# print(max)
# print(arr.index(max)+1)

# 세번째 시도
arr = []
for i in range(9):
    arr.append(int(input()))
max = arr[0]
for i in arr:
    if max < i:
        max = i
print(max)
print(arr.index(max)+1)

# 처음에 틀린 이유
# max 변수를 arr[0]이라는 값이없는 함수로 초기화하여 런타임 오류가 난듯 보인다.

# 두번째 틀린 이유
# i 와 비교가 되는 max 변수가 존재하지 않아서 런타임 오류가 난듯 보인다.
