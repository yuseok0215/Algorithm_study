from collections import deque
import time
import sys
input = sys.stdin.readline
start_time = time.time() #측정 시작

n,k = map(int, input().split())
graph = []
target = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] != 0:
            target.append((temp[j], 0, i, j))
    graph.append(temp)

s,x,y = map(int, input().split())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def spread_virus(num,x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 0:
            graph[nx][ny] = num

target.sort()

def bfs():
    q = deque(target)
    
    while q:
        virus, time, x, y = q.popleft()

        if time == s:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus
                    q.append(virus, time+1, nx, ny)
                
print(graph[x-1][y-1])   
end_time = time.time() #측정종료
print("time :", end_time - start_time) #수행 시간 출력