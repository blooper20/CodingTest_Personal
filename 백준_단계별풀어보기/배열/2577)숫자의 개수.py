# 문제
# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# 예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고,
# 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.

# 입력
# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.

# 출력
# 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다.
# 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.


# 예제 입력
# 150
# 266
# 427

# 예제 출력 1
# 3
# 1
# 0
# 2
# 0
# 0
# 0
# 2
# 0
# 0

# 첫번째 시도
a = int(input())
b = int(input())
c = int(input())
n0 = 0
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
n6 = 0
n7 = 0
n8 = 0
n9 = 0
abc = a * b * c
abcList = []
for i in str(abc):
    abcList.append(i)
for j in abcList:
    if j == '0':
        n0 += 1
    if j == '1':
        n1 += 1
    if j == '2':
        n2 += 1
    if j == '3':
        n3 += 1
    if j == '4':
        n4 += 1
    if j == '5':
        n5 += 1
    if j == '6':
        n6 += 1
    if j == '7':
        n7 += 1
    if j == '8':
        n8 += 1
    if j == '9':
        n9 += 1
print(n0)
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)
print(n6)
print(n7)
print(n8)
print(n9)
