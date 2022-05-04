# 문제
# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.
# 입력의 마지막에는 0이 주어진다.

# 출력
# 각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

# 제한
# 1 ≤ n ≤ 123,456

# 예제 입력 1
# 1
# 10
# 13
# 100
# 1000
# 10000
# 100000
# 0

# 예제 출력 1
# 1
# 4
# 3
# 21
# 135
# 1033
# 8392

# 첫번째 시도
# def isPrime(num):
#     if num == 1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#         return True
# stopFlag = 1
# while stopFlag == 1:
#     n = int(input())
#     sosu = []
#     if n == 0:
#         stopFlag = 0
#     else:
#         for i in range(n, (2*n+1)):
#             if isPrime(i):
#                 sosu.append(i)
#     if n != 0:
#         print(len(sosu))
#     else:
#         break

# 정답
def sosu(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True  # 소수 구하는 방식은 위와 같다


all_list = list(range(2, 246912))  # 문제에서 제한한 범위
memo = []  # for문 밖에 리스트 정의

for i in all_list:  # 2부터 2*123,456 범위
    if sosu(i):  # sosu함수에 해당하면
        memo.append(i)  # 리스트에 추가

n = int(input())

while True:
    count = 0  # 갯수를 세야하는 조건 때문에 카운트
    if n == 0:
        break
    for i in memo:  # memo리스트 중에서
        if n < i <= 2*n:  # 입력한 값의 범위 내에서 값이 있으면
            count += 1  # 있을 때 마다 카운트 +1
    print(count)
    n = int(input())  # 0 입력받기 전까지 계속 해야하므로 입력 받음
