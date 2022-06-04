# 문제
# (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
# (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

# 출력
# 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

# 예제 입력 1
# 472
# 385

# 예제 출력 1
# 2360
# 3776
# 1416
# 181720

# 첫번째 시도
upNum = int(input())
downNum = list(input())
ten = 1
a = []
answer = 0
for num in downNum[::-1]:
    result = upNum * int(num)
    print(result)
    a.append(result)
for n in a:
    total = ten * n
    answer += total
    ten *= 10
print(answer)
