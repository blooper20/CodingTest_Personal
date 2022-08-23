# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
# 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

# 예제 입력 1
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

# 예제 출력 1
# 1
# 1
# 0
# 0
# 1

# 정답
N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
A.sort()			# A 정렬

# arr의 각 원소별로 이분탐색
for num in arr:
    lt, rt = 0, N - 1		# lt는 맨 앞, rt는 맨 뒤
    isExist = False		# 찾음 여부

    # 이분탐색 시작
    while lt <= rt:		# lt가 rt보다 커지면 반복문 탈출
        mid = (lt + rt) // 2  # mid는 lt와 rt의 중간값
        if num == A[mid]:  # num(목표값)이 A[mid]값과 같다면 (목표값 존재여부를 알았다면)
            isExist = True  # isExist Ture 변경
            print(1)		# 1 출력
            break		# 반복문 탈출
        elif num > A[mid]:  # A[mid]가 num보다 작으면
            lt = mid + 1  # lt를 높임
        else:			# A[mid]가 num보다 크다면
            rt = mid - 1  # rt를 낮춤

    if not isExist:		# 찾지 못한 경우
        print(0)		# 0 출력
