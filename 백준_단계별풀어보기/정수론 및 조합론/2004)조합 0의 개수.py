# 문제
#  
# $n \choose m$의 끝자리 $0$의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 $n$, $m$ ($0 \le m \le n \le 2,000,000,000$, $n \ne 0$)이 들어온다.

# 출력
# 첫째 줄에
# $n \choose m$의 끝자리 $0$의 개수를 출력한다.

# 예제 입력 1
# 25 12

# 예제 출력 1
# 2

# 정답
n, m = map(int, input().split())


def cnt2(n):
    n2 = 0
    while(n != 0):
        n //= 2
        n2 += n
    return n2


def cnt5(n):
    n5 = 0
    while(n != 0):
        n //= 5
        n5 += n
    return n5


print(min(cnt2(n)-cnt2(m)-cnt2(n-m), cnt5(n)-cnt5(m)-cnt5(n-m)))
