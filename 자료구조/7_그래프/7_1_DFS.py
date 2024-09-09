
# 백준 - 바이러스
# DFS, 재귀함수 사용, 전역변수 cnt 사용, defaultdict 사용

from collections import defaultdict

n = int(input())
v = int(input())
graph = []
adj_list = defaultdict(list)
visited = set()
cnt = 0

for _ in range(v):
    graph.append(list(map(int, input().split())))

for k, val in graph:
    adj_list[k].append(val)
    adj_list[val].append(k)


def dfs(node):
    global cnt
    visited.add(node)
    cnt += 1

    for n in adj_list[node]:
        if n not in visited:
            dfs(n)

dfs(1)
print(cnt - 1)