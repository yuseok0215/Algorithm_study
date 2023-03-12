from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int, input().split())
graph = []
target = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            target.append((graph[i][j], 0, i, j))

s,x,y = map(int, input().split())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

target.sort()

q = deque(target)

while q:
    virus, time, a, b = q.popleft()

    if time == s:
        break

    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]

        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append(virus, time+1, nx, ny)

                
print(graph[x-1][y-1])   
