import time
start_time = time.time() #측정 시작

N, M = map(int,input().split())
bowling = list(map(int, input().split()))

count = 0
for i in range(1,N+1):
    if bowling.count(i) >= 2:
        a = bowling.count(i)
        count += (a*(a-1))/2

print(int(((N*(N-1))/2)-count))

end_time = time.time() #측정종료
print("time :", end_time - start_time) #수행 시간 출력