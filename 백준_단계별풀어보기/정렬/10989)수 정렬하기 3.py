# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1
# 10
# 5
# 2
# 3
# 1
# 4
# 2
# 3
# 5
# 1
# 7

# 예제 출력 1
# 1
# 1
# 2
# 2
# 3
# 3
# 4
# 5
# 5
# 7

# 첫번째 시도
# n = int(input())
# sortList = []
# for _ in range(n):
#     a = int(input())
#     sortList.append(a)
# sortList.sort()
# for i in sortList:
#     print(i)

# 정답
import sys

n = int(input())  # 입력받는 수의 개수 n
n_list = [0] * 10001  # 리스트크기 <= 10000
for i in range(n):
    n_list[int(sys.stdin.readline())] += 1
for i in range(10001):
    if n_list[i] != 0:
        for j in range(n_list[i]):
            print(i)
