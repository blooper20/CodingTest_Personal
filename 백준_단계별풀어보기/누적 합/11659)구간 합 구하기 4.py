# 문제
# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

# 출력
# 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

# 제한
# 1 ≤ N ≤ 100,000
# 1 ≤ M ≤ 100,000
# 1 ≤ i ≤ j ≤ N

# 예제 입력 1
# 5 3
# 5 4 3 2 1
# 1 3
# 2 4
# 5 5

# 예제 출력 1
# 12
# 9
# 1

# 첫번째 시도
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# nList = list(map(int, input().split()))
# for _ in range(m):
#     a, b = map(int, input().split())
#     print(sum(nList[a-1:b]))

# 정답
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0]*(n+1)  # 인덱스 혼동 때문에 n+1로(인덱스 0은 0으로 사용x)
for k in range(1, n+1):
    dp[k] = dp[k-1]+arr[k-1]  # 합 미리 구하기
for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j]-dp[i-1])  # j번째~i번째
