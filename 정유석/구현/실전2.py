import time
start_time = time.time() #측정 시작

n,m = map(int, input().split())
x,y,dir = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
visited[x][y] = True

dx = [-1,0,1,0] 
dy = [0,1,0,-1]

cnt = 1 # 현재 위치 포함
turn_cnt = 0
while True:
    dir -= 1

    if dir == -1:
        dir = 3

    nx = x + dx[dir]
    ny = y + dx[dir]

    if graph[nx][ny] == 0 and not visited[nx][ny]:
        visited[nx][ny] = True
        x = nx
        y = ny
        cnt += 1
        turn_cnt = 0 # 초기화
        continue
    else:
        turn_cnt += 1
    
    if turn_cnt == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]

        if graph[nx][ny] == 0 and not visited[nx][ny]:
            x = nx
            y = ny
            turn_cnt = 0
        else:
            print(cnt)
            break

end_time = time.time() #측정종료
print("time :", end_time - start_time) #수행 시간 출력