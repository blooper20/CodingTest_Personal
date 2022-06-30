# 문제
# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.
# 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.
# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

# 출력
# 듣보잡의 수와 그 명단을 사전순으로 출력한다.

# 예제 입력 1
# 3 4
# ohhenrie
# charlie
# baesangwook
# obama
# baesangwook
# ohhenrie
# clinton

# 예제 출력 1
# 2
# baesangwook
# ohhenrie

# 첫번째 시도
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# listen = []
# listenLook = []
# for _ in range(n):
#     li = input()
#     listen.append(li)
# for _ in range(m):
#     lo = input()
#     if lo in listen:
#         listenLook.append(lo)
# print(len(listenLook))
# for answer in listenLook:
#     print(answer)

# 두번째 시도
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# listen = set()
# listenLook = set()
# for _ in range(n):
#     li = input()
#     listen.add(li)
# for _ in range(m):
#     lo = input()
#     if lo in listen:
#         listenLook.add(lo)
# print(len(listenLook))
# for answer in listenLook:
#     print(answer)

# 정답
N, M = map(int, input().split())
arr_1 = set()
arr_2 = set()

for _ in range(N):
    arr_1.add(input())
for _ in range(M):
    arr_2.add(input())

arr = sorted(list(arr_1 & arr_2))
print(len(arr))

for i in arr:
    print(i)
