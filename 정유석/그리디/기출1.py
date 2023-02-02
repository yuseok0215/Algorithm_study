n = int(input())
arr = list(map(int, input().split()))

arr.sort()

group = 0
cnt = 0 # 현재 그룹

for elem in arr:
    cnt += 1
    if cnt >= elem:
        group += 1
        cnt = 0

print(group)



