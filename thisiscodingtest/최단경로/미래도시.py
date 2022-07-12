INF = int(1e9)

n,m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기자신으로 가는 값 0으로 초기화
for a in range(1,n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 비용(1)로 초기화
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    


x, k = map(int, input().split())

# K번 회사를 방문, 그 다음 X번 회사 방문
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행결과
distance = graph[1][k] + graph[k][x]

if distance == INF:
    print("-1")
else:
    print(distance)

