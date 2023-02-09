import time
start_time = time.time() #측정 시작

N, M = map(int, input().split())
column = []

for i in range(N):
    c = list(map(int, input().split()))
    column.append(min(c))

print(max(column))

end_time = time.time() #측정종료
print("time :", end_time - start_time) #수행 시간 출력