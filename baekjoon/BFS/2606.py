from collections import deque

n = int(input())
m = int(input())

graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))

visited = [False] * m

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    cnt = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt
    


print(bfs(graph, 1, visited))
    
