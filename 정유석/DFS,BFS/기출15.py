from collections import deque

n,m,k,x = map(int, input().split())
roads = [[] for _ in range(n+1)]
for _ in range(m):
    start,end = map(int, input().split())
    roads[start].append(end)

dist = [-1] * (n+1)
dist[x] = 0

q = deque()
q.append(x)

while q:
    start = q.popleft()
    for end in roads[start]:
        if dist[end] == -1:
            dist[end] = dist[start] + 1
            q.append(end)
    
flag = False
for i in range(n+1):
    if dist[i] == k:
        print(i)
        flag = True

if flag == False:
    print(-1)