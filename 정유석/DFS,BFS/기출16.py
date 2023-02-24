from collections import deque
import copy
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

max_cnt = 0

def bfs():
    global max_cnt

    q = deque()
    temp = copy.deepcopy(graph)

    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q.append((i,j))
    
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                q.append((nx,ny))
    # 안전구역 개수
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                cnt += 1
    
    max_cnt = max(cnt, max_cnt)

def make_wall(count):

    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(count+1)
                graph[i][j] = 0

make_wall(0)
print(max_cnt)
    
        