import time
start_time = time.time() #측정 시작

# n = int(input())

# n_str = str(n)
# n_len = len(n_str) // 2

# left_sum = 0
# right_sum = 0
# for i in range(n_len):
#     left_sum += int(n_str[i])

# for i in range(n_len, len(n_str)):
#     right_sum += int(n_str[i])

# if left_sum == right_sum:
#     print('LUCKY')
# else:
#     print('READY')

n = input()
length = len(n)
summary = 0

for i in range(length // 2):
    summary += int(n[i])

for i in range(length // 2, length):
    summary -= int(n[i])

if summary == 0:
    print('LUCKY')
else:
    print('READY')


end_time = time.time() #측정종료
print("time :", end_time - start_time) #수행 시간 출력