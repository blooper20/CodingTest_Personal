# 문제
# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
# n=17일때 까지 피보나치 수를 써보면 다음과 같다.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n이 주어진다. n은 1,000,000,000,000,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 n번째 피보나치 수를 1,000,000,007으로 나눈 나머지를 출력한다.

# 예제 입력 1
# 1000

# 예제 출력 1
# 517691607

# 정답
import sys
input = sys.stdin.readline
p = 1000000007
# 제곱을 구하는 분할정복


def power(adj, n):
    if n == 1:
        return adj
    elif n % 2:
        return multi(power(adj, n-1), adj)
    else:
        return power(multi(adj, adj), n//2)
# 행렬의 곱셈


def multi(a, b):
    temp = [[0]*len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum = 0
            for k in range(2):
                sum += a[i][k]*b[k][j]
            temp[i][j] = sum % p
    return temp


# 초기 행렬
adj = [[1, 1], [1, 0]]
# 피보나치 초기값
start = [[1], [1]]
n = int(input())
if n < 3:
    print(1)
else:
    print(multi(power(adj, n-2), start)[0][0])
