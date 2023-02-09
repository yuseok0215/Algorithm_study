from collections import deque

n = int(input())
k = int(input()) # 사과의 개수

graph = [[0] * n for _ in range(n)]

for _ in range(k):
    a,b = map(int, input().split())
    graph[a-1][b-1] = 1  # 사과 위치 표시

l = int(input())
direction = []
for _ in range(l):
    t, direct = input().split()
    t = int(t)
    direction.append((t,direct))

snake = deque()
snake.append((0,0)) # 길이 1, 시작 위치
x,y =0,0

dx = [-1,0,1,0]
dy = [0,1,0,-1] # 북동남서

time = 0
snake_dir = 1 # 시작은 동쪽 방향 dx,dy의 idx 
dir_idx = 0

while True:
    time += 1
    # 다음 위치로 뱀의 머리 이동
    nx = x + dx[snake_dir]
    ny = y + dy[snake_dir]

    # 그래프 범위를 벗어나거나 뱀의 꼬리에 닿았을 때
    if nx<0 or nx>=n or ny<0 or ny>=n or (nx,ny) in snake:
        break

    # 다음 위치 추가
    snake.appendleft((nx,ny))
    # 머리 위치 변경
    x = nx
    y = ny

    if graph[nx][ny] == 0: # 사과가 없을때 꼬리 제거
        snake.pop()
    else:
        graph[nx][ny] = 0
    
    if time == direction[dir_idx][0]: # 뱀의 방향 회전
        if direction[dir_idx][1] == 'D':
            snake_dir += 1
            if snake_dir == 4:
                snake_dir = 0
        else:
            snake_dir -= 1
            if snake_dir == -1:
                snake_dir = 3
        if dir_idx < l-1:
            dir_idx += 1 # 다음 전환 시점으로 변경

print(time)   
        



