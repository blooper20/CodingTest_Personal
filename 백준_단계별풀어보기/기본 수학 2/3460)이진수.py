# 문제
# 양의 정수 n이 주어졌을 때, 이를 이진수로 나타냈을 때 1의 위치를 모두 찾는 프로그램을 작성하시오. 최하위 비트(least significant bit, lsb)의 위치는 0이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, n이 주어진다. (1 ≤ T ≤ 10, 1 ≤ n ≤ 106)

# 출력
# 각 테스트 케이스에 대해서, 1의 위치를 공백으로 구분해서 줄 하나에 출력한다. 위치가 낮은 것부터 출력한다.

# 예제 입력 1
# 1
# 13

# 예제 출력 1
# 0 2 3

# 첫번째 시도
# t = int(input())
# for _ in range(t):
#     one = 0
#     answer = []
#     n = int(input())
#     b = list(bin(n)[2:])
#     for i in b:
#         if i == '1':
#             answer.append(one)
#         one += 1
#     print(*answer)

# 두번째 시도
t = int(input())
for _ in range(t):
    one = 0
    answer = []
    n = int(input())
    b = list(bin(n)[2:])
    for i in b[::-1]:
        if i == '1':
            answer.append(one)
        one += 1
    print(*answer)
