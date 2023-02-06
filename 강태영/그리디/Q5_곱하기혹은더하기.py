import time
start_time = time.time() #측정 시작

S = input()

result = int(S[0])

for i in range(1,len(S)):
    if(result*int(S[i])>=result+int(S[i])):
        result *= int(S[i])
    else:
        result += int(S[i])

print(result)

end_time = time.time() #측정종료
print("time :", end_time - start_time) #수행 시간 출력