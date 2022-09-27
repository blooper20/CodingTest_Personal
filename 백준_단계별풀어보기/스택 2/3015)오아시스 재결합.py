# 문제
# 오아시스의 재결합 공연에 N명이 한 줄로 서서 기다리고 있다.
# 이 역사적인 순간을 맞이하기 위해 줄에서서 기다리고 있던 백준이는 갑자기 자기가 볼 수 있는 사람의 수가 궁금해 졌다.
# 두 사람 A와 B가 서로 볼 수 있으려면, 두 사람 사이에 A 또는 B보다 키가 큰 사람이 없어야 한다.
# 줄에 서있는 사람의 키가 주어졌을 때, 서로 볼 수 있는 쌍의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 줄에서 기다리고 있는 사람의 수 N이 주어진다. (1 ≤ N ≤ 500,000)
# 둘째 줄부터 N개의 줄에는 각 사람의 키가 나노미터 단위로 주어진다. 모든 사람의 키는 231 나노미터 보다 작다.
# 사람들이 서 있는 순서대로 입력이 주어진다.

# 출력
# 서로 볼 수 있는 쌍의 수를 출력한다.

# 예제 입력 1
# 7
# 2
# 4
# 1
# 2
# 2
# 5
# 1

# 예제 출력 1
# 10

# 정답
import sys
HEIGHT, CNT = 0, 1


def solve():
    stack = []
    answer = 0

    for h in arr:
        # stack에 현재 사람보다 작은 사람이 있으면 pop하고 answer에 추가
        while stack and stack[-1][HEIGHT] < h:
            answer += stack.pop()[CNT]

        # 스택이 비었으면 현재 사람을 그냥 추가
        if not stack:
            stack.append((h, 1))
            continue

        # 스택이 안 비었고, top과 지금 현재 사람의 키가 같으면
        if stack[-1][HEIGHT] == h:
            cnt = stack.pop()[CNT]
            answer += cnt

            # 현재 같은키보다 왼쪽이 있으므로 -> top과 현재 사람이 볼 수 있으므로 1추가
            if stack:
                answer += 1

            # 현재 키인 사람과 같은 사람이 cnt만큼 있으므로, 키 = h, 명수 = cnt+1를 스택에 추가
            stack.append((h, cnt + 1))

        # 스택이 안비었고, 왼쪽 사람보다 키가 작으므로 그 사람만 볼 수 있음 -> 스택에 현재 키를 넣고, answer에 1추가(왼쪽 사람만 볼 수 있으므로)
        else:
            stack.append((h, 1))
            answer += 1

    return answer


N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
print(solve())
