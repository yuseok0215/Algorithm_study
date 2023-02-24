from collections import deque

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

visited = [[False] * m for _ in range(n)]

# def dfs(x,y,dist,visited):
#     visited[x][y] = True

#     if x==n-1 and y==m-1:
#         return dist

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1 and not visited[nx][ny]:
#             dfs(nx,ny,dist+1,visited)

# result = dfs(0,0,1,visited)
# print(result)    

def bfs(a,b):
    q = deque()
    q.append((a,b))

    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

bfs(0,0)
print(graph[n-1][m-1])