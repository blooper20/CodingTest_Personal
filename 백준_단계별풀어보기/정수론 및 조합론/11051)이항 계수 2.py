# 문제
# 자연수 (N)과 정수 (K)가 주어졌을 때 이항 계수를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 (N)과 (K)가 주어진다. (1 ≤ (N) ≤ 1,000, 0 ≤ (K) ≤ (N))

# 출력
# 이항계수를 10,007로 나눈 나머지를 출력한다.

# 예제 입력 1
# 5 2

# 예제 출력 1
# 10

# 정답
from math import factorial
n, k = map(int, input().split())
result = factorial(n) // (factorial(k) * factorial(n - k))
print(result % 10007)
