# 문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.

# 예제 입력 1
# 5 5
# 5 7
# 7 5

# 예제 출력 1
# 7 7

# 예제 입력 2
# 30 20
# 10 10
# 10 20

# 예제 출력 2
# 30 10

# 첫번째 시도
xList = []
yList = []
for _ in range(3):
    x, y = map(int, input().split())
    xList.append(x)
    yList.append(y)
if xList.count(x) != 1:
    for _ in range(2):
        xList.remove(x)
if yList.count(y) != 1:
    for _ in range(2):
        yList.remove(y)
print(xList[-1], yList[-1])
