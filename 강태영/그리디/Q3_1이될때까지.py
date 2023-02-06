import time
start_time = time.time() #측정 시작

N, K = map(int, input().split())
count = 0

while(N != 1):
    if(N%K == 0):
        N //= K
    else:
        N -= 1
    count += 1

print(count)

end_time = time.time() #측정종료
print("time :", end_time - start_time) #수행 시간 출력