# 문제
# 오늘도 서준이는 깊이 우선 탐색(DFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.
# N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.
# 깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.

# dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
#     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
#     for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
#         if (visited[x] = NO) then dfs(V, E, x);
# }
# 입력
# 첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)이 주어진다.
# 다음 M개 줄에 간선 정보 u v가 주어지며 정점 u와 정점 v의 가중치 1인 양방향 간선을 나타낸다. (1 ≤ u < v ≤ N, u ≠ v) 모든 간선의 (u, v) 쌍의 값은 서로 다르다.

# 출력
# 첫째 줄부터 N개의 줄에 정수를 한 개씩 출력한다. i번째 줄에는 정점 i의 방문 순서를 출력한다. 시작 정점의 방문 순서는 1이다. 시작 정점에서 방문할 수 없는 경우 0을 출력한다.

# 예제 입력 1
# 5 5 1
# 1 4
# 1 2
# 2 3
# 2 4
# 3 4
# 예제 출력 1
# 1
# 2
# 3
# 4
# 0

# 정답
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 내림차순인 인접 그래프를 스택에 하나씩 넣어주면, 나중에 스택에서
# 꺼낼때는 이들을 오름차순으로 꺼내게 됨
for i in range(1, len(graph)):
    graph[i].sort(reverse=True)


def DFS(start):
    stack = [start]
    visited = [-1]*(N+1)
    result = [0]*(N+1)  # result[idx]는 idx노드를 방문한 순서 값을 의미함
    cnt = 1  # 방문 순서 값

    while stack:
        cnt_node = stack.pop()
        # 사이클이 있는 그래프 같은 경우에,
        # 어떤 노드에 대해, 그 노드의 인접 노드 K를 스택에 넣어
        # 놓은 뒤에, DFS를 수행하다가 더 깊은 깊이의 어느 노드에서
        # 인접 노드로 K를 또 스택에 넣는 경우가 생김.
        # 이 때의 K가 먼저 스택에서 꺼내져 처리되므로,
        # 맨 첨 넣어줬던 K는 스택에서 꺼낸 뒤 따로 코드를
        # 수행해주지 않고 넘어감
        if visited[cnt_node] == 1:
            continue

        visited[cnt_node] = 1

        # 방문 순서 값 저장
        result[cnt_node] = cnt
        cnt += 1

        # 아직 방문 이력 없으면(=스택에서 뽑은 적 없으면)
        # 스택에 싹 다 집어 넣기
        for adj_node in graph[cnt_node]:
            if visited[adj_node] == -1:
                stack.append(adj_node)

    return result


result = DFS(R)

print(*result[1:], sep="\n")
