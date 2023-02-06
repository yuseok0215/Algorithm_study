import time
start_time = time.time() #측정 시작

N = int(input())
fear_arr = list(map(int, input().split()))

fear_arr.sort() #정렬

result = 0 #그룹의 수 
count = 0 #모험가의 수
for i in fear_arr:
    count += 1
    if count >= i: #현재 그룹의 모험가 수보다 현재 공포도 이상이면 그룹 결성 및 새로운 그룹 형성
        result += 1
        count = 0

print(result)

end_time = time.time() #측정종료
print("time :", end_time - start_time) #수행 시간 출력