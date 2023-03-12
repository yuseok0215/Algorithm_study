import sys
input = sys.stdin.readline

n = int(input())
graph = []
teacher = 0
for _ in range(n):
  data = list(map(input().split()))
  teacher += data.count('T')
  graph.append(data)

# 상,하,좌,우 움직이는 배열
dx = [1,-1, 0, 0]
dy = [0, 0, 1, -1]

# 직선 방향 확인 함수
def check_S(x,y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 직선 방향으로 확인
    while 0<= nx < n and 0<= ny < n and graph[nx][ny] !='O':
      if graph[nx][ny] == 'S':
        return True            
      else:        
        nx += dx[i]
        ny += dy[i]
  return False

def dfs(count):
  global answer
  if count == 3:
    cnt = 0
    for i in range(n):
      for j in range(n):
        if graph[i][j] == 'T':
          if not check_S(i,j):          
            cnt+=1
    # 모든 선생이 감시가 불가능할 때
    if cnt == teacher:
      answer = True
    return

  for i in range(n):
    for j in range(n):
      if graph[i][j] == 'X':
        graph[i][j] = 'O'
        dfs(count+1)
        graph[i][j] = 'X'

answer = False
dfs(0)
if answer:
  print('YES')
else:
  print('NO')