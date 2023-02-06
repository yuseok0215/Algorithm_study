import time
start_time = time.time() #측정 시작

S = input()

count0 = 0 #모두 0으로 바꾸는 경우
count1 = 0 #모두 1로 바꾸는 경우

#첫 번째 원소 처리
if S[0] == '0': 
    count1 += 1
else:
    count0 += 1 

#두 번재 원소부터 비교
for i in range(1,len(S)):
    if S[i-1] != S[i]:
        if S[i] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))


end_time = time.time() #측정종료
print("time :", end_time - start_time) #수행 시간 출력