# 문제
# 히스토그램은 직사각형 여러 개가 아래쪽으로 정렬되어 있는 도형이다. 각 직사각형은 같은 너비를 가지고 있지만, 높이는 서로 다를 수도 있다.
# 예를 들어, 왼쪽 그림은 높이가 2, 1, 4, 5, 1, 3, 3이고 너비가 1인 직사각형으로 이루어진 히스토그램이다.
# 히스토그램에서 가장 넓이가 큰 직사각형을 구하는 프로그램을 작성하시오.

# 입력
# 입력은 테스트 케이스 여러 개로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, 직사각형의 수 n이 가장 처음으로 주어진다. (1 ≤ n ≤ 100,000)
# 그 다음 n개의 정수 h1, ..., hn (0 ≤ hi ≤ 1,000,000,000)가 주어진다.
# 이 숫자들은 히스토그램에 있는 직사각형의 높이이며, 왼쪽부터 오른쪽까지 순서대로 주어진다.
# 모든 직사각형의 너비는 1이고, 입력의 마지막 줄에는 0이 하나 주어진다.

# 출력
# 각 테스트 케이스에 대해서, 히스토그램에서 가장 넓이가 큰 직사각형의 넓이를 출력한다.

# 예제 입력 1
# 7 2 1 4 5 1 3 3
# 4 1000 1000 1000 1000
# 0

# 예제 출력 1
# 8
# 4000

# 정답
import math
import sys


# sys.setrecursionlimit(10 ** 8)  # pypy 제출시 삭제!
def input(): return sys.stdin.readline().rstrip()


# in_range = lambda y,x: 0<=y<n and 0<=x<m
MAX = 1000000000


def make_seg(idx, s, e):
    if s == e:
        seg[idx] = histograms[s]
        return seg[idx]

    # w = e-s+1
    mid = (s + e) // 2
    l = make_seg(idx * 2, s, mid)
    r = make_seg(idx * 2 + 1, mid + 1, e)
    seg[idx] = min(l, r)
    return seg[idx]


def f(frm, to):
    if frm == to:
        return histograms[frm]

    mid = (frm + to) // 2
    l = f(frm, mid)
    r = f(mid + 1, to)

    max_val = max(l, r)

    # including border
    h = min(histograms[mid], histograms[mid + 1])
    w = 2
    s = w * h
    i, j = mid, mid + 1
    while frm < i or j < to:  # i==frm and j==to 가 되면 종료
        if j == to or frm < i and histograms[i - 1] >= histograms[j + 1]:
            i -= 1
            w += 1
            h = min(h, histograms[i])
            s = max(s, w * h)
        else:
            j += 1
            w += 1
            h = min(h, histograms[j])
            s = max(s, w * h)

    max_val = max(max_val, s)

    return max_val


while True:
    inp = list(map(int, input().split()))
    n = inp[0]
    if n == 0:
        break
    histograms = inp[1:]

    b = math.ceil(math.log2(n)) + 1
    node_n = 1 << b
    seg = [0] * node_n  # 구간의 min h 를 가짐
    make_seg(1, 0, len(histograms) - 1)

    print(f(0, len(histograms) - 1))
