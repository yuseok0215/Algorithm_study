import time
start_time = time.time() #측정 시작

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

#정렬-내림차순
arr.sort(reverse=True)

first = arr[0]#가장 큰 수
second = arr[1]#두번째로 큰 수

#가장 큰 수가 더해지는 횟수 게산
count = int(M/(K+1))*K
count += M % (K+1)

result = 0
result += (count)*first #가장 큰 수 더하기
result += (M-count)*second #두 번째로 큰 수 더하기

print(result)

end_time = time.time() #측정종료
print("time :", end_time - start_time) #수행 시간 출력