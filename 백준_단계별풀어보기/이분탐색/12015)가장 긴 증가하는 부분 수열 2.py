# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000,000)이 주어진다.
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000,000)

# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

# 예제 입력 1
# 6
# 10 20 10 30 20 50

# 예제 출력 1
# 4

# 정답
import sys


def find(target):
    l, h = 1, len(stack)-1
    while l < h:
        m = (l+h)//2
        if stack[m] < target:
            l = m+1
        elif stack[m] > target:
            h = m
        else:
            l = h = m
    return h


l = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = [0]

for a in arr:
    if stack[-1] < a:
        stack.append(a)
    else:
        stack[find(a)] = a

print(len(stack)-1)
