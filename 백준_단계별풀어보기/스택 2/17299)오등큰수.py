# 문제
# 크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오등큰수 NGF(i)를 구하려고 한다.
# Ai가 수열 A에서 등장한 횟수를 F(Ai)라고 했을 때, Ai의 오등큰수는 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다.
# 그러한 수가 없는 경우에 오등큰수는 -1이다.
# 예를 들어, A = [1, 1, 2, 3, 4, 2, 1]인 경우 F(1) = 3, F(2) = 2, F(3) = 1, F(4) = 1이다.
# A1의 오른쪽에 있으면서 등장한 횟수가 3보다 큰 수는 없기 때문에, NGF(1) = -1이다.
# A3의 경우에는 A7이 오른쪽에 있으면서 F(A3=2) < F(A7=1) 이기 때문에, NGF(3) = 1이다. NGF(4) = 2, NGF(5) = 2, NGF(6) = 1 이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째에 수열 A의 원소 A1, A2, ..., AN (1 ≤ Ai ≤ 1,000,000)이 주어진다.

# 출력
# 총 N개의 수 NGF(1), NGF(2), ..., NGF(N)을 공백으로 구분해 출력한다.

# 예제 입력 1
# 7
# 1 1 2 3 4 2 1

# 예제 출력 1
# -1 -1 1 2 2 1 -1

# 정답
from collections import Counter
from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
nums_count = Counter(nums)
result = [-1] * n
stack = [0]

for i in range(1, n):
    while stack and nums_count[nums[stack[-1]]] < nums_count[nums[i]]:
        result[stack.pop()] = nums[i]
    stack.append(i)

print(*result)
