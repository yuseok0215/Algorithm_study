import time
start_time = time.time() #측정 시작

N = int(input())
coins = list(map(int,input().split()))
coins.sort()

target = 1
for x in coins:
    print(x, target)
    if target < x:
        break
    target += x

print(target)

end_time = time.time() #측정종료
print("time :", end_time - start_time) #수행 시간 출력